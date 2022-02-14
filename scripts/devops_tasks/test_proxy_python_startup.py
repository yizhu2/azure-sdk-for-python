import requests
import time
import os
import shlex
import subprocess

CONTAINER_NAME = "ambitious_azsdk_test_proxy"
LINUX_IMAGE_SOURCE_PREFIX = "azsdkengsys.azurecr.io/engsys/testproxy-lin"
WINDOWS_IMAGE_SOURCE_PREFIX = "azsdkengsys.azurecr.io/engsys/testproxy-win"
CONTAINER_STARTUP_TIMEOUT = 6000
PROXY_MANUALLY_STARTED = os.getenv("PROXY_MANUAL_START", False)

PROXY_URL = os.getenv("PROXY_URL", "https://localhost:5001")
REPO_ROOT = os.path.abspath(os.path.join(os.path.abspath(__file__), "..", "..", "..", ".."))
PROXY_CHECK_URL = PROXY_URL.rstrip("/") + "/Info/Available"
TOOL_ENV_VAR = "PROXY_PID"


def check_availability():
    # type: () -> None
    """Attempts request to /Info/Available. If a test-proxy instance is responding, we should get a response."""
    try:
        response = requests.get(PROXY_CHECK_URL, timeout=60)
        return response.status_code
    # We get an SSLError if the container is started but the endpoint isn't available yet
    except requests.exceptions.SSLError as sslError:
        return 404
    except Exception as e:
        print(e)
        return 404


def check_proxy_availability():
    # type: () -> None
    """Waits for the availability of the test-proxy."""
    start = time.time()
    now = time.time()
    status_code = 0
    while now - start < CONTAINER_STARTUP_TIMEOUT and status_code != 200:
        status_code = check_availability()
        now = time.time()


def start_test_proxy():
    # type: () -> None
    """Starts the test proxy and returns when the proxy server is ready to receive requests. In regular use
    cases, this will auto-start the test-proxy docker container. In CI, or when environment variable TF_BUILD is set, this
    function will start the test-proxy .NET tool."""

    if not PROXY_MANUALLY_STARTED:
        if os.getenv("TF_BUILD"):
            print("Starting the test proxy tool...")
            if check_availability() == 200:
                print("Tool is responding, exiting...")
            else:
                envname = os.getenv("TOX_ENV_NAME", "default")
                log = open("_proxy_log_{}.log".format(envname), "a")
                proc = subprocess.Popen(
                    shlex.split('test-proxy --storage-location="{}" --urls "{}"'.format(REPO_ROOT, PROXY_URL))
                    stdout=log,
                    stderr=log,
                )
                os.environ[TOOL_ENV_VAR] = str(proc.pid)
        else:
            print("Starting the test proxy container...")

        # Wait for the proxy server to become available
        check_proxy_availability()

def invoke_test_proxy_version():
    proc = subprocess.Popen(
        shlex.split('test-proxy --version'),
        capture_output=True
        # stdout=log,
        # stderr=log,
    )
    proc.communicate()

if __name__ == "__main__":
    start_test_proxy()
    