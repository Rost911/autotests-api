from swagger_coverage_tool import SwaggerCoverageTracker

# Initialize the tracker for our "api-course" service
# IMPORTANT: 'api-course' must exactly match the `key` in SWAGGER_COVERAGE_SERVICES
tracker = SwaggerCoverageTracker(service="api-course")