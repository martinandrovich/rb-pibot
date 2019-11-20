# Commands

## Usage

The following commands can be transmitted via TCP at port `:8080`, but will require an initial authentication with the correct password. Using bash and socat, an example command could be:

```bash
echo getdist | socat - tcp:192.168.99.<group number>
```

## Command table

| Command       | Description                                             |
| ------------- | ------------------------------------------------------- |
| `auth <pswd>` | Authenticate using the password `<pswd>`                |
| `getdist`     | Return the last distance value from the distance sensor |
| `getmotors`   | Return the current control values used on the motors    |
| `start`       | Start wall following behavior                           |
| `stop`        | Stop the robot                                          |
