import re
import urllib2
import urllib
from bs4 import BeautifulSoup as BS

def download_plugins(plugins, url='http://updates.jenkins-ci.org/download/plugins/'):
    for plugin in plugins:
        urllib.urlretrieve(url+plugin[0]+'/'+plugin[1]+'/'+plugin[0]+'.hpi',plugin[0]+'.hpi')
        
def build_deps(url):
    html = urllib2.urlopen(url)
    bs_obj = BS(html, 'html.parser')
    table = bs_obj.find('table', {'class': 'confluenceTable'}).tbody.find_all('tr')[1].td
    deps = table.get_text()
    deps = re.findall(r'(version\:[0-9\.\,\sa-zA-Z]+)\)', deps)
    deps_links = table.find_all('a', href=re.compile(r'(https:\/\/wiki\.jenkins-ci\.org/display/JENKINS/)(.+)'))
    clean_deps_links = [[d.get_text(), d.get('href')] for d in deps_links]
    full_deps = zip(deps, clean_deps_links)
    return full_deps
    
def main():
  
    download = []

    html = urllib2.urlopen('https://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin')
    bs_obj = BS(html, 'html.parser')
    table = bs_obj.find('table', {'class': 'confluenceTable'}).tbody.find_all('tr')[1].td

    plugin_id = bs_obj.find('table', {'class': 'confluenceTable'}).tbody.find_all('tr')[0].td.get_text().strip()
    plugin_version = table.find_all('a')[0].get_text()

    download.append((plugin_id,plugin_version))

    dependencies = build_deps('https://wiki.jenkins-ci.org/display/JENKINS/Git+Plugin')
    for fd in dependencies:
        download.append((fd[1][0],fd[0].split(':')[1].split(',')[0]))
            
    download_plugins(plugins=download)

if __name__ == '__main__':
    main()
