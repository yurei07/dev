import subprocess
import shutil
import os

def zip_folder(source_folder: str, zip_name: str):
    shutil.make_archive(zip_name.replace(".zip", ""), "zip", source_folder)

def run_rclone_sync(remote: str, local: str) -> str:
    try:
        archive_name = "backup.zip"
        zip_folder(local,archive_name)

        result = subprocess.run(
                ['rclone', 'sync', remote, local, '--progress', '--transfers 8', '--drive-chunk-size 64M'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
        )

        if os.path.exists(archive_name):
            os.remove(archive_name)

        if result.returncode == 0:
            return "✅ Синхронизация завершена успешно."
        else:
            return f"❌ Ошибка при синхронизации:\n{result.stderr}"
    except Exception as e:
        return f"⚠️ Ошибка выполнения rclone: {e}"
