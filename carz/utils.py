# function to get value from google secret manager
def access_secret_version(secret_name, client, project_id, version_id="latest", ):
    client = client
    name = f"projects/{project_id}/secrets/{secret_name}/versions/{version_id}"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")
