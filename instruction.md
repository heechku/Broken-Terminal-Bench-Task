There is an access log at /app/access.log. Analyze the traffic and write a JSON summary to /app/report.json with these fields:

1. total_requests must equal the number of log lines.
2. unique_ips must equal the number of distinct client IPs.
3. top_path must be the single most-requested path.