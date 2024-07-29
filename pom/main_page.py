from playwright.sync_api import expect
from config import playwright_config

class MainPage:
    def __init__(self, page):
        self.page = page
        self.mediahuisProject = page.locator('div').filter(has_text='Mediahuis Publishing Studio').first
        self.mediahuisProjectLink = page.locator('#projects').get_by_role('link')
        self.mediahuisProjectText = page.get_by_role('heading', name= 'Mediahuis') 
        self.iOProject = page.locator('div').filter( has_text= 'iO A end-to-end agency for').first 
        self.iOProjectLink = page.locator('#projects').get_by_role('link') 
        self.iOProjectText = page.get_by_role('heading', name= 'iO', exact= True) 
        self.responsumProject = page.locator('div').filter( has_text= 'Responsum T&M A software').first 
        self.responsumProjectLink = page.locator('#projects').get_by_role('link')
        self.responsumProjectText= page.get_by_role('heading', name= 'Responsum T&M') 
        self.linkedinLink = page.get_by_role('link', name= 'Linkedin') 
        self.githubLink = page.get_by_role('link', name= 'GitHub') 
        self.icons8Link = page.get_by_role('link', name= 'Icons8') 
        self.brightestLink = page.get_by_role('link', name= 'Brightest') 
        self.brightestPlaywrightCourseLink = page.get_by_role('link', name= 'training course')
        self.heading = page.get_by_role('heading', name= "Hello I'm Robbert") 
        self.resumeButton = page.get_by_role('link', name= 'RESUME') 
        self.mobileHamburgerMenuButton = page.locator('div').filter( has_text= 'PROJECTS SKILLS CONTACT RESUME').locator('div') 
        self.mobileCloseMenuButton = page.locator('span')
        self.projectsLinkNavbar = page.get_by_role('link', name= 'PROJECTS') 
        self.skillsLinkNavbar = page.get_by_role('link', name= 'SKILLS') 
        self.contactLinkNavbar = page.get_by_role('link', name= 'CONTACT') 
        self.logo = page.locator('#logo').get_by_role('link') 
        self.connectWithMeButton = page.get_by_role('link', name= 'Connect With Me') 
        self.contactEmailLink = page.get_by_role('link', name= 'robbert.champagne1@gmail.com') 
        self.navbar = page.get_by_role("navigation")

    def navigate(self):
        self.page.goto(playwright_config.config["base_url"])

    def checkHeadingText(self):
        expect(self.heading).to_contain_text("Hello I'm Robbert")
