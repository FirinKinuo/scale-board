import requests


def get_weight(server: str) -> float:
    """
    Get weight from weight server
    Args:
        server: str: URL for getting weight data

    Returns:
        float: Received weight from the server

    Raises:
        ValueError - If the weight was not received or an error was received
        RequestException - In case of an error when sending a request
    """
    response = requests.get(url=server)

    if response.status_code == 200:
        if 'ves' in response.text:
            return float(response.text.replace('ves:', ''))

    raise ValueError(f"Error getting data: Status: {response.status_code} || Message: {response.text}")
