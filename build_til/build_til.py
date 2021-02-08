"Run this after build_database.py - it needs til.db"
import pathlib
import sqlite_utils
import sys
import re
import os
import shutil

root = pathlib.Path(__file__).parent.resolve().parents[0]


index_re = re.compile(r"<!\-\- index starts \-\->.*<!\-\- index ends \-\->", re.DOTALL)
count_re = re.compile(r"<!\-\- count starts \-\->.*<!\-\- count ends \-\->", re.DOTALL)

COUNT_TEMPLATE = "<!-- count starts -->{}<!-- count ends -->"

if __name__ == "__main__":
    db = sqlite_utils.Database(root / "build_til/til.db")

    # Update TIL main page
    index = ["<!-- index starts -->"]

    # add recently added
    index.append("## Recently Added\n")
    for i, row in enumerate(db["til"].rows_where(order_by="created_utc DESC")):
        if i < 5:
            # print("* row['title']")
            title = row['title']
            url = row['url']
            
            # update url to be relative to site root
            url_parts = url.split('/')
            topic = url_parts[-2]
            file_name = url_parts[-1].split('.')[0]
            url_updated = f'/til/{topic}/{file_name}'

            date=row["created"].split("T")[0]
            index.append(f"* [{title} ({topic})]({url_updated}) - {date}")
        else:
            index.append
            break

    by_topic = {}
    for row in db["til"].rows_where(order_by="created_utc"):
        by_topic.setdefault(row["topic"], []).append(row)
    
    for topic, rows in by_topic.items():
        index.append("## {}\n".format(topic))
        for row in rows:
            title = row['title']
            url = row['url']
            
            # update url to be relative to site root
            url_parts = url.split('/')
            topic = url_parts[-2]
            file_name = url_parts[-1].split('.')[0]
            url_updated = f'/til/{topic}/{file_name}'

            date=row["created"].split("T")[0]

            index.append(f"* [{title}]({url_updated}) - {date}")
        index.append("")
    if index[-1] == "":
        index.pop()
    index.append("<!-- index ends -->")
    if "--rewrite" in sys.argv:
        til_page = root / "_pages/til.md"
        index_txt = "\n".join(index).strip()
        til_contents = til_page.open().read()
        rewritten = index_re.sub(index_txt, til_contents)
        rewritten = count_re.sub(COUNT_TEMPLATE.format(db["til"].count), rewritten)
        til_page.open("w").write(rewritten)
    else:
        print("\n".join(index))


    # create md files for the til's from the database
    if "--rewrite" in sys.argv:
        for row in db["til"].rows_where(order_by="created_utc"):
            shutil.rmtree(root / "_til")
            os.makedirs(root / "_til" / row["topic"], exist_ok=True)
            with open(root / "_til" / row["topic"] / row["url"].split('/')[-1], 'w+') as f:
                f.write("---\n")
                f.write(f'title: \"{row["title"]} ({row["topic"]})\"')
                f.write("\n")
                f.write("---\n")
                f.write(row["body"])