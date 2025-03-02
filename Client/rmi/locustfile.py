from locust import HttpUser, task, events, between
import subprocess
import time  # Import the time module to measure response time

class RMIClientUser(HttpUser):
    @task
    def test_rmi_service(self):
        # Record the start time
        start_time = time.time()

        # Run the Java RMI client as a subprocess
        result = subprocess.run(
            ["java", "RMIClient"], 
            capture_output=True, 
            text=True, 
            check=True
        )
            
        # Calculate the response time (in milliseconds)
        response_time = (time.time() - start_time) * 1000  # Convert to milliseconds
        response_length = len(result.stdout)  # Length of the output for response size

        # Fire the request success event with the response time
        events.request.fire(
            request_type="RMI", 
            name="RMIClient Test", 
            response_time=response_time,
            response_length=response_length
        )
