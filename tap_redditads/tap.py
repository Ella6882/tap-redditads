"""RedditAds tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_redditads import streams


class TapRedditAds(Tap):
    """RedditAds tap class."""

    name = "tap-redditads"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "account_id",
            th.StringType,
            required=True,
            secret=True,
            description="Account ID for Reddit Ads API.",
        ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://ads-api.reddit.com/api/v3/ad_accounts",
            description="URL for Reddit Ads API.",
        ),
        th.Property(
            "client_id",
            th.StringType,
            required=True,
            secret=True,
            description="Client ID for Reddit Ads API.",
        ),
        th.Property(
            "client_secret",
            th.StringType,
            required=True,
            secret=True,
            description="Client Secret for Reddit Ads API.",
        ),
        th.Property(
            "refresh_token",
            th.StringType,
            required=True,
            description="Refresh token for Reddit Ads API.",
        ),
        th.Property(
            "user_agent",
            th.StringType,
            required=True,
            description=(
                "A custom User-Agent header to send with each request. Format is {{Target platform}}:{{Unique app ID}}:{{Version string}} (by /u/{{Your Reddit username}})."
            ),
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            default="2023-01-01",
            description="The earliest record date to sync.",
        ),
        th.Property(
            "breakdown_columns",
            th.ArrayType(th.StringType),
            default=["campaign_id", "date"],
            description=(
                "Reddit Ads report API breakdown field names. "
                "Must align with columns in the reports stream schema."
            ),
        ),
    ).to_dict()


    def discover_streams(self) -> list[streams.RedditAdsStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.AdsStream(self),
            streams.CampaignsStream(self),
            streams.ReportCampaignDateStream(self),
        ]


if __name__ == "__main__":
    TapRedditAds.cli()
