import csv

def get_column_rows(csv_path, col, start_line, stop_line, encoding="utf-8"):
    """
    csv_path   : CSVファイルのパス
    col        : 列番号（0始まり）
    start_line : 開始行番号（0始まり）
    stop_line  : 終了行番号
                 ・0以上 → 上から数えた行番号（含む）
                 ・負数  → 最終行からの相対位置（-1 が最終行）
    """
    with open(csv_path, newline="", encoding=encoding) as f:
        rows = list(csv.reader(f))

    total_lines = len(rows)

    # stop_line が負の場合は、最終行からの相対位置に変換
    if stop_line < 0:
        stop_line = total_lines + stop_line
        # 念のため下限をクリップ
        stop_line = max(stop_line, 0)

    values = []
    for line_idx in range(start_line, min(stop_line + 1, total_lines)):
        values.append(rows[line_idx][col])

    return values

