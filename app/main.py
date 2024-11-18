import uvicorn
from fastapi import FastAPI, Query
from starlette.responses import FileResponse

app = FastAPI()


@app.get("/apk/update_demo_1.0.2.apk")
async def download_apk():
    filename = "/datas/apk/update_demo_1.0.2.apk"
    return FileResponse(filename, filename="update_demo_1.0.2.apk")


@app.get("/check/{version}")
def check_update(version: str):
    return {
        "Code": 0,
        "Msg": "",
        "UpdateStatus": 1,
        "VersionCode": 3,
        "VersionName": "1.0.2",
        "ModifyContent": "1、优化api接口。\r\n2、添加使用demo演示。\r\n3、新增自定义更新服务API接口。\r\n4、优化更新提示界面。",
        "DownloadUrl": "https://raw.githubusercontent.com/xuexiangjys/XUpdate/master/apk/xupdate_demo_1.0.2.apk",
        "ApkSize": 2048,
        "ApkMd5": ""
    }


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
