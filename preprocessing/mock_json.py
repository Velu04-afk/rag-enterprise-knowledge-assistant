import csv
import json

# -----------------------------
# CONFIG
# -----------------------------
INPUT_CSV = 'datasets/train.csv'
OUTPUT_JSON = 'data.json'
MAX_RECORDS = 100

# -----------------------------
# MAIN LOGIC
# -----------------------------


def csv_to_json(input_csv, output_json, max_records):
    dataset = []

    with open(input_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for idx, row in enumerate(reader):
            if idx >= max_records:
                break

            question = row.get('Question') or row.get('title') or 'No question'
            answer = row.get('Answer') or row.get('body') or 'No answer'
            type = row.get('qtype') or 'No answer'

            data = {

                "question": question,
                "answer": answer,
                "type": type
            }

            dataset.append(data)

    with open(output_json, 'w', encoding='utf-8') as outfile:
        json.dump(dataset, outfile, indent=2)

    print(
        f"✅ Saved {len(dataset)} question and answers {output_json}")


if __name__ == "__main__":
    csv_to_json(INPUT_CSV, OUTPUT_JSON, MAX_RECORDS)
