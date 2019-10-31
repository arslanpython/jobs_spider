import re

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from jobs.items import JobItem
from jobs.mysql.job_helper import JobHelper


class JobParser:
    RE_NAME = r'(.*\))|(.*)\sis|(.*)\s\W|(.*?\s.*?\s)'
    RE_LOCATION = r'\sin\s(.*)|\sat\s(.*)'
    RE_POSITION = r'ing\s(.*)\sin|ing\s(.*)'

    job_helper = JobHelper()
    job_ids = job_helper.get_ids()

    def parse(self, response):
        new_jobs = []
        job_ids = response.css('.athing::attr(id)').getall()
        raw_jobs = response.css('.storylink::text').getall()

        for job_id, raw_job in zip(job_ids, raw_jobs):
            if (job_id, ) in self.job_ids:
                continue
            job = JobItem()
            job['job_id'] = self.clean(job_id)
            job['name'] = self.get_company_name(raw_job)
            job['location'] = self.get_location(raw_job)
            job['position'] = self.get_position(raw_job)

            new_jobs.append(job)
            yield job

        self.job_helper.insert(new_jobs)

        urls_s = response.css('.morelink')
        yield from [response.follow(url_s, callback=self.parse) for url_s in urls_s]

    def get_company_name(self, raw_job):
        return self.clean(re.search(self.RE_NAME, raw_job, flags=re.I).groups(''))

    def get_location(self, raw_job):
        return self.clean(re.findall(self.RE_LOCATION, raw_job, flags=re.I))

    def get_position(self, raw_job):
        return self.clean(re.findall(self.RE_POSITION, raw_job, flags=re.I))

    def clean(self, data):
        if isinstance(data, tuple):
            return [e.strip() for e in data if e and e.strip()][0]

        if isinstance(data, list):
            data = [e.strip() for seq in data for e in seq if e and e.strip()]
            return data[0] if data else ''

        if isinstance(data, str):
            return data.strip()


class JobsSpider(CrawlSpider):
    name = 'jobs'
    job_parser = JobParser()

    allowed_domains = [
        'ycombinator.com',
    ]
    start_urls = [
        'https://news.ycombinator.com/jobs',
    ]

    rules = [
        Rule(LinkExtractor(restrict_css='.morelink')),
    ]

    def parse(self, response):
        yield from super().parse(response)

        return self.job_parser.parse(response)
