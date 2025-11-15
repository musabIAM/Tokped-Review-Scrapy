import scrapy
import json

class TokpedReviewSpider(scrapy.Spider):

    name = "tokped_review"
    allowed_domains = ["gql.tokopedia.com"]
    
    SHOP_ID = "2718180"  # Change to target shop ID
    API_URL = "https://gql.tokopedia.com/graphql/ReviewList"
    LIMIT_PER_PAGE = 10
    
    def start_requests(self):
        yield self.make_request(page=1)
    
    def make_request(self, page):
        payload = [
            {
                "operationName": "ReviewList",
                "variables": {
                    "shopID": self.SHOP_ID,
                    "page": page,
                    "limit": self.LIMIT_PER_PAGE,
                    "sortBy": "create_time desc",
                    "filterBy": ""
                },
                    "query": """query ReviewList($shopID: String!, $limit: Int!, $page: Int!, $filterBy: String, $sortBy: String) {
                productrevGetShopReviewReadingList(shopID: $shopID, limit: $limit, page: $page, filterBy: $filterBy, sortBy: $sortBy) {
                list {
                    id: reviewID
                    product {
                    productID
                    productName
                    productImageURL
                    productPageURL
                    productStatus
                    isDeletedProduct
                    productVariant {
                        variantID
                        variantName
                        __typename
                    }
                    __typename
                    }
                    rating
                    reviewTime
                    reviewText
                    reviewerID
                    reviewerName
                    avatar
                    replyText
                    replyTime
                    attachments {
                    attachmentID
                    thumbnailURL
                    fullsizeURL
                    __typename
                    }
                    videoAttachments {
                    attachmentID
                    videoUrl
                    __typename
                    }
                    state {
                    isReportable
                    isAnonymous
                    __typename
                    }
                    likeDislike {
                    totalLike
                    likeStatus
                    __typename
                    }
                    badRatingReasonFmt
                    __typename
                }
                hasNext
                shopName
                totalReviews
                __typename
                }
                }"""
                }
            ]
            
        return scrapy.Request(
                self.API_URL,
                method="POST",
                body=json.dumps(payload),
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                },
                meta={"page": page},
                callback=self.parse
                
            )
    
    def parse(self, response):
        
        try:
            data = json.loads(response.text)
            data = data[0]
       
            reviews_data = data.get("data").get("productrevGetShopReviewReadingList")
            reviews_list = reviews_data.get("list")
            
            # Yield each review as an item
            for review in reviews_list:
                yield {
                    "review_id": review.get("id"),
                    "product_id": review.get("product").get("productID"),
                    "product_name": review.get("product").get("productName"),
                    "product_image": review.get("product").get("productImageURL"),
                    "product_url": review.get("product").get("productPageURL"),
                    "rating": review.get("rating"),
                    "review_time": review.get("reviewTime"),
                    "review_text": review.get("reviewText"),
                    "reviewer_id": review.get("reviewerID"),
                    "reviewer_name": review.get("reviewerName"),
                    "reviewer_avatar": review.get("avatar"),
                    "reply_text": review.get("replyText"),
                    "reply_time": review.get("replyTime"),
                    "total_likes": review.get("likeDislike").get("totalLike"),
                    "like_status": review.get("likeDislike").get("likeStatus"),
                    "is_anonymous": review.get("state").get("isAnonymous"),
                    "attachments": review.get("attachments"),
                    "video_attachments": review.get("videoAttachments"),
                    "bad_rating_reason": review.get("badRatingReasonFmt"),
                }
            
            # Check if there are more pages and continue scraping
            has_next = reviews_data.get("hasNext")
            if has_next:
                next_page = response.meta.get("page") + 1
                yield self.make_request(page=next_page)
            else:
                self.logger.info(f"No more pages. Total reviews in shop: {reviews_data.get('totalReviews')}")
                
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to parse JSON: {e}")
        except Exception as e:
            self.logger.error(f"Error parsing response: {e}")
