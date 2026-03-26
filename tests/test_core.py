from tap_redditads.tap import TapRedditAds
from tap_redditads.streams import ReportCampaignDateStream  # Assuming you have this stream for reports

SAMPLE_CONFIG = {
    "start_date": "2024-01-01T00:00:00Z",
    "client_id": "valid_client_id",
    "client_secret": "valid_client_secret",
    "refresh_token": "valid_refresh_token",
    "account_id": "your_account_id",
    "user_agent": "cloud:tap-reddit-ads:0.1.0 (by /u/ellar_81)",
    "breakdown_columns": ["campaign_id", "date"],
}

def test_reports_post_process():
    """Test that report data is processed correctly after fetching."""
    # Example of raw data from Reddit Ads API (mocked for testing)
    row = {
        "campaign_id": "123",
        "date": "2024-07-15",
        "impressions": 1000,
        "metrics_updated_at": "2025-04-09T23:22:51.601000+00:00"
    }

    # Assuming ReportsStream handles data from "reports"
    reports_stream = ReportCampaignDateStream(tap=TapRedditAds(config=SAMPLE_CONFIG))

    # Apply post_process to simulate processing the raw row data
    post_processed_row = reports_stream.post_process(row)

    # Assertions to ensure correct processing
    assert post_processed_row["impressions"] == 1000  # Ensure the impressions are correct
    assert post_processed_row["campaign_id"] == "123"  # Ensure region is correctly processed
    assert post_processed_row["metrics_updated_at"] == "2025-04-09T23:22:51.601000+00:00"  # Ensure timestamp is intact

