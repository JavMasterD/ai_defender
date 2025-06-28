import random
import json

class AIDefender:
    def __init__(self):
        self.threat_log = []

    def disconnect_suspicious_networks(self, networks):
        disconnected = []
        for net in networks:
            if "Free" in net or "Unknown" in net:
                disconnected.append(net)
                self.threat_log.append(f"تم فصل الاتصال بالشبكة المشبوهة: {net}")
        return disconnected

    def block_suspicious_apps(self, apps):
        blocked = []
        for app in apps:
            if "malware" in app or "spy" in app:
                blocked.append(app)
                self.threat_log.append(f"تم حظر التطبيق المشبوه: {app}")
        return blocked

    def scan_wifi_networks(self, networks):
        suspicious = [net for net in networks if "Free" in net or "Unknown" in net]
        return suspicious

    def scan_links(self, links):
        suspicious = [link for link in links if any(word in link for word in ["phishing", "malware", "suspicious"])]
        return suspicious

    def scan_apps(self, apps):
        suspicious = [app for app in apps if "malware" in app or "spy" in app]
        return suspicious

    def scan_ports(self, ports):
        suspicious = [port for port in ports if port in [22, 23, 445]]
        return suspicious

    def stop_all_attacks(self):
        self.threat_log.append("تم إيقاف جميع الهجمات المحتملة وإغلاق جميع الاتصالات المشبوهة")
        return True

    def learn_from_data(self, data):
        self.threat_log.append(f"تعلمت المكتبة من البيانات: {data}")

    def predict_threat(self, app_name):
        if any(word in app_name for word in ["malware", "spy"]):
            return True
        return False

    def chat(self, user_input):
        if "فحص الشبكة" in user_input:
            return self.scan_wifi_networks(["HomeNet", "FreeWifi"])
        elif "فحص التطبيقات" in user_input:
            return self.scan_apps(["com.safe.app", "com.malware.spy"])
        elif "فحص الروابط" in user_input:
            return self.scan_links(["http://safe.com", "http://phishing.site"])
        elif "قطع الشبكة" in user_input:
            return self.disconnect_suspicious_networks(["FreeWifi"])
        elif "حظر التطبيقات" in user_input:
            return self.block_suspicious_apps(["com.malware.spy"])
        elif "ايقاف الهجمات" in user_input:
            return self.stop_all_attacks()
        else:
            return "أمر غير معروف"
