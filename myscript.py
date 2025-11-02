import os
bad_hash = os.environ.get("GITHUB_SHA")
good_hash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

os.system(f"git bisect start {bad_hash} {good_hash}")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")