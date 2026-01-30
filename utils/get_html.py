import sqlite3


def get_region_html(region_name):
    try:
        conn = sqlite3.connect('../national_db')
        cursor = conn.cursor()

        cursor.execute("""
            SELECT r.id, r.name, h.[htmls-log] 
            FROM regions r 
            LEFT JOIN htmls h ON r.id = h.region_id 
            WHERE r.name = ?
        """, (region_name,))

        data = cursor.fetchone()
        conn.close()

        if not data:
            return {"error": f"Region '{region_name}' not found"}

        region_id, name, html = data

        result = {
            "region_id": region_id,
            "name": name,
            "html_found": html is not None
        }

        if html:
            result["html"] = html
        return result

    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}
