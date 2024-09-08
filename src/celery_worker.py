from src.config.celery_config import celery_app
from src.services.Crawler.main import AutoCrawler

@celery_app.task
def run_crawler(skip: bool = True, threads: int = 4, google: bool = True, naver: bool = True,
                full_resolution: bool = False, face: bool = False, no_gui: str = 'auto',
                limit: int = 0, proxy_list: str = ''):
    
    # Split the proxy list into a list of strings
    proxy_list = proxy_list.split(',') if proxy_list else None

    # Determine the no_gui value based on the full_resolution flag
    if no_gui == 'auto':
        _no_gui = full_resolution
    elif no_gui == 'true':
        _no_gui = True
    else:
        _no_gui = False

    # Print out the options for logging/debugging
    print(f"Running AutoCrawler with options: skip={skip}, threads={threads}, google={google}, naver={naver}, "
          f"full_resolution={full_resolution}, face={face}, no_gui={_no_gui}, limit={limit}, proxy_list={proxy_list}")

    # Initialize the AutoCrawler with provided parameters
    crawler = AutoCrawler(skip_already_exist=skip, n_threads=threads, do_google=google, do_naver=naver,
                          full_resolution=full_resolution, face=face, no_gui=_no_gui, limit=limit, 
                          proxy_list=proxy_list)
    
    # Run the crawling process
    crawler.do_crawling()

    return {"status": "Crawling finished"}
