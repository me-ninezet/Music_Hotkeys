from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
import logging
import psutil

class AppVolumeController:
    def __init__(self, app_name='Yandex.Music'):
        self.app_name = app_name
        self.session = self._find_session()

    def _find_session(self):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process:
                process_name = session.Process.name()
                # Более гибкий поиск (Yandex.exe, YandexMusic.exe, etc.)
                if self.app_name.lower() in process_name.lower():
                    return session
                # Альтернативные имена
                elif "yandex" in process_name.lower() and "music" in process_name.lower():
                    return session
                elif "яндекс" in process_name.lower() and "музыка" in process_name.lower():
                    return session
                elif "y" in process_name.lower() and "music" in process_name.lower():
                    return session
        # logging.error(f"Session for {self.app_name} not found")
        return None

    def set_volume(self, level):
        if self.session:
            try:
                volume = self.session._ctl.QueryInterface(ISimpleAudioVolume)
                volume.SetMasterVolume(max(0.0, min(1.0, level)), None)
                return True
            except Exception as e:
                logging.error(f"Error setting volume: {e}")
        return False

    def get_volume(self):
        if self.session:
            try:
                volume = self.session._ctl.QueryInterface(ISimpleAudioVolume)
                return volume.GetMasterVolume()
            except Exception as e:
                logging.error(f"Error getting volume: {e}")
        return 0

    def refresh_session(self):
        """Обновить сессию (на случай перезапуска приложения)"""
        self.session = self._find_session()
        return self.session is not None

    def mute(self):
        if self.session:
            volume = self.session._ctl.QueryInterface(ISimpleAudioVolume)
            volume.SetMute(True, None)

    def unmute(self):
        if self.session:
            volume = self.session._ctl.QueryInterface(ISimpleAudioVolume)
            volume.SetMute(False, None)

    def list_all_audio_sessions(self):
        """Вывести все доступные аудио-сессии для отладки"""
        sessions = AudioUtilities.GetAllSessions()
        for i, session in enumerate(sessions):
            if session.Process:
                print(f"{i}: {session.Process.name()} (PID: {session.ProcessId})")
            else:
                print(f"{i}: System session")
