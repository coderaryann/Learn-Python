def http_status (status):
  match status:
    case 200:
      return "ok"
    case 404:
      return "Not found"
    case 500:
      return "Internal Server Error"
    case _:
      return "Unknown status"
      # Usage
print (http_status (200))  # Output: Ok
print (http_status (404))  # Output: Not found
print (http_status (200))  # Output: Internal Server Error
print (http_status (403))  # Output: Unknown status