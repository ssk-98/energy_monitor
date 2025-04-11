from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/devices')
def list_devices():
    df = pd.read_csv('../../energy_usage.csv')  # Accessing the file from the parent directory
    devices = df[df['power_consumption'].notna()]['device_id'].dropna().unique().tolist()
    return jsonify(devices)

@app.route('/api/device/<device_id>')
def device_stats(device_id):
    df = pd.read_csv('../../energy_usage.csv')  # Accessing the file from the parent directory
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    device_df = df[(df['device_id'] == device_id) & (df['power_consumption'].notna())]
    if device_df.empty:
        return jsonify({"error": "No data found for device"}), 404

    latest = device_df.sort_values('timestamp', ascending=False).iloc[0]
    average = device_df['power_consumption'].mean()
    peak_row = device_df.loc[device_df['power_consumption'].idxmax()]

    stats = {
        "type": "device",
        "id": device_id,
        "latest_power": latest['power_consumption'],
        "latest_time": latest['timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
        "average_power": round(average, 2),
        "peak_power": peak_row['power_consumption'],
        "peak_time": peak_row['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
    }

    return jsonify(stats)

@app.route('/api/sources')
def list_sources():
    df = pd.read_csv('../../energy_usage.csv')  # Accessing the file from the parent directory
    sources = df[df['power_generated'].notna()]['energy_source'].dropna().unique().tolist()
    return jsonify(sources)

@app.route('/api/source/<source_id>')
def source_stats(source_id):
    df = pd.read_csv('../../energy_usage.csv')  # Accessing the file from the parent directory
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    source_df = df[(df['energy_source'] == source_id) & (df['power_generated'].notna())]
    if source_df.empty:
        return jsonify({"error": "No data found for source"}), 404

    latest = source_df.sort_values('timestamp', ascending=False).iloc[0]
    average = source_df['power_generated'].mean()
    peak_row = source_df.loc[source_df['power_generated'].idxmax()]

    stats = {
        "type": "source",
        "id": source_id,
        "latest_power": latest['power_generated'],
        "latest_time": latest['timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
        "average_power": round(average, 2),
        "peak_power": peak_row['power_generated'],
        "peak_time": peak_row['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
    }

    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)