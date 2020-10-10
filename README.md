# Unraid-Diskstate-Checker
first foray into Docker Containers

Useful environment variables:
UNRAID_URL: the ip address of the unraid tower to poll
LOGIN_USERNAME: the root login username (default root)
LOGIN_PASSWORD: the root login password (feels insecure but I haven't found a better way besides not doing it)

default communication port for the server is on port 8000

<details>
  <summary>
    Some useful docker commands for the future
  </summary>
  
  ```
  docker build --tag [name] .
  docker run --env name=value -p hostport:containerport [name]
  ```
</details>
