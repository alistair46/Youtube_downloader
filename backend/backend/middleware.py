import os

class FileCleanupMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Check if response has the attribute to clean up the file
        if hasattr(response, 'cleanup_file'):
            file_path = response.cleanup_file
            if os.path.exists(file_path):
                os.remove(file_path)
        return response
