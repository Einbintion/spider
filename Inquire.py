import pandas as pd

def get_product_by_id(csv_path: str, product_id: int) -> dict:
    """
    从 CSV 文件中通过商品ID查找商品信息。

    参数:
        csv_path (str): CSV 文件路径
        product_id (int): 要查找的商品ID（整数格式）

    返回:
        pd.DataFrame: 匹配到的商品信息（可能为空）
    """
    # 1) 读取 CSV，先把商品ID当成字符串读进来
    df = pd.read_csv(csv_path, dtype={"商品ID": str})

    # 2) 统一把科学计数法和“.0”去掉，并跳过空值
    def normalize_id(x):
        if pd.isna(x) or x.strip()=="":
            return ""
        try:
            return str(int(float(x)))
        except:
            # 如果仍然有无法转换的，原样返回
            return x.strip()

    df["商品ID"] = df["商品ID"].apply(normalize_id)

    # 3) 目标 ID 转成字符串
    target = str(product_id)

    # 4) 过滤
    result = df[df["商品ID"] == target]
    if not result.empty:
        record = result.to_dict(orient="records")[0]
        return record


if __name__ == '__main__':
    csv_file = "书包商品.csv"
    res = get_product_by_id(csv_file, 666990585455)
    print(res)
