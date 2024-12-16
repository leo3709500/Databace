# 監理站管理系統

## 簡介
本系統是一個使用 PyQt5 開發的桌面應用程式，旨在提升監理站的管理效率，提供友好的圖形化用戶界面。透過此應用程式，用戶可以進行資料查詢、管理員登入、車輛和違規狀態的新增、修改、刪除等操作。

---

## 系統需求
- **Python 版本**：Python 3.x
- **套件依賴**：PyQt5

---

## 安裝與設定

### 安裝步驟
1. 確保已安裝 Python 3.x。
   - 可以至 [Python 官網](https://www.python.org/downloads/) 下載並安裝。
2. 使用 pip 安裝 PyQt5：
   ```bash
   pip install PyQt5
   ```
3. 從 GitHub 或專案來源下載或克隆此專案：
   ```bash
   git clone <專案網址>
   ```
4. 進入專案目錄，檢查文件結構是否完整。

---

## 使用說明

### 啟動應用程式
1. 確保所有依賴已安裝。
2. 執行 `main_controller.py` 啟動應用程式：
   ```bash
   python main_controller.py
   ```
3. 系統將開啟主視窗，提供多項功能選擇。

---

### 功能介紹

#### 主視窗功能
- **一般查詢**：進入用戶查詢界面，用於查詢監理站相關數據。
- **管理員登入**：提供管理員登入入口，需輸入憑證進行身分驗證。
- **一般常見問題**：查看常見問題，提供用戶快速獲取解答。
- **其他監理站**：查看其他監理站的相關資訊。

#### 管理員功能
登入成功後，管理員可以操作以下功能：

1. **新增使用者**
   - 輸入新用戶的個人資料並提交至系統。
2. **新增車輛**
   - 登記新車輛資訊，包括車牌號、車型等基本資訊。
3. **新增違規狀態**
   - 記錄車輛或駕駛人的違規行為。
4. **查詢**
   - 搜尋系統內的現有資料，支持多條件篩選。
5. **刪除**
   - 選擇並刪除不再需要的數據記錄。
6. **修改**
   - 對現有數據進行編輯和更新。

#### 返回功能
- 各個功能界面均提供「返回」按鈕，用於快速返回主畫面，提升操作便利性。

---

## 文件結構
專案包含以下主要文件與目錄：

- **`back/`**
  - 資料庫相關腳本，負責與後端資料庫進行交互。
- **`mac_buttons.py`**
  - 定義適用於 macOS 的按鈕樣式及操作。
- **`main_controller.py`**
  - 主控制器，負責應用程式的整體邏輯及界面切換。
- **`main_window.py`**
  - 主視窗的 UI 定義文件。
- **`login_window.py`**
  - 管理員登入視窗的 UI 定義文件。
- **`manage_window.py`**
  - 管理員專用的操作界面，包括新增、刪除、修改功能。
- **`add.py`**
  - 新增使用者界面。
- **`add_vehicle.py`**
  - 新增車輛界面。
- **`add_violation.py`**
  - 新增違規狀態界面。
- **`user_find.py`**
  - 用戶查詢界面。
- **`question.py`**
  - 常見問題界面。
- **`other.py`**
  - 顯示其他監理站資訊的界面。

---

## 注意事項

1. **UI 文件注意**
   - 本應用程式的 UI 文件是由 PyQt5 的 `pyuic` 工具生成。
   - 若需更改界面設計，建議修改源 `.ui` 文件後重新生成對應的 Python 文件：
     ```bash
     pyuic5 -x <source.ui> -o <output.py>
     ```
   - 手動更改生成的 Python 文件可能在重新生成時丟失。

2. **資料庫連接**
   - 資料庫連線配置文件位於 `back` 資料夾內。
   - 修改資料庫連線資訊前，請備份原始文件。
   - 確保資料庫主機地址、用戶名及密碼正確無誤。

3. **系統相容性**
   - 本應用程式主要測試於 Windows 和 macOS 環境。
   - 若於其他系統上執行，可能需額外配置依賴。

4. **錯誤排除**
   - 啟動應用程式時出現錯誤，請檢查 Python 版本及所需模組是否安裝完整。
   - 如遇 UI 顯示異常，確認 PyQt5 是否為最新版本。

---

## 更新日誌

### v1.0.0
- 初始版本釋出。
- 提供基本功能包括：主視窗導航、管理員登入、新增與查詢資料功能。

---

