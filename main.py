import json
import psycopg2


if __name__ == '__main__':
    # 事前に取得したQiitaの記事一覧がJSONとしてあるので読み込む
    with open("./qiita_items_page_1.json") as f:
        qiita_items = json.load(f)

    # Connect to your postgres DB
    conn = psycopg2.connect("host=localhost user=postgres password=testpasswordhagiwarashohei")
    cur = conn.cursor()

    # DBに入れていく
    for qiita_item in qiita_items:

        # Execute a query
        title = qiita_item['title'].replace("'", "''")
        rendered_body = qiita_item['rendered_body'].replace("'", "''")
        cur.execute(
            "INSERT INTO qiita_items (id, title, rendered_body, created_at, url) " +
            f"VALUES('{qiita_item['id']}', '{title}', '{rendered_body}', '{qiita_item['created_at']}', '{qiita_item['url']}');")

    conn.commit()
