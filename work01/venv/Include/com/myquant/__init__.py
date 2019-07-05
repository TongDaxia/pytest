import Download_HistoryStock
import StockCode

if __name__ == '__main__':
    code = StockCode.StockCode()
    code_list = code.run()
    print("-------------",code_list)

    for temp_code in code_list:
        time.sleep(1)
        download = Download_HistoryStock(temp_code)
        download.run()