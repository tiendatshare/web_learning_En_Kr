import os
import sys
import json
import psutil

if len(sys.argv) < 3:
    print("Usage: python lock-manager.py <lock_path> <acquire|release> [operation_name]")
    sys.exit(1)

lock_path = sys.argv[1]
action = sys.argv[2]

if action == 'acquire':
    op = sys.argv[3] if len(sys.argv) > 3 else 'unknown'
    if os.path.exists(lock_path):
        try:
            with open(lock_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if psutil.pid_exists(data['pid']):
                print(f"Error: LockHeld by {data['operation']} (PID {data['pid']})")
                sys.exit(1)
        except Exception:
            pass  # Overwrite stale or corrupted lock file
            
    # Write lockfile
    try:
        pid = int(sys.argv[4]) if len(sys.argv) > 4 else os.getppid()
        dirname = os.path.dirname(lock_path)
        if dirname:
            os.makedirs(dirname, exist_ok=True)
        with open(lock_path, 'w', encoding='utf-8') as f:
            json.dump({"pid": pid, "operation": op}, f)
        print(f"Lock acquired successfully for PID {pid}")
    except Exception as e:
        print(f"Error creating lockfile: {e}")
        sys.exit(1)

elif action == 'release':
    if os.path.exists(lock_path):
        try:
            os.remove(lock_path)
            print("Lock released successfully")
        except Exception as e:
            print(f"Error releasing lock: {e}")
            sys.exit(1)
    else:
        print("No lockfile existed")

else:
    print(f"Unknown action: {action}")
    sys.exit(1)
