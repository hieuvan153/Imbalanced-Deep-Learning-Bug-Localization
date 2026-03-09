from collections import namedtuple
from pathlib import Path

_DATASET_ROOT = Path(r"E:\Desktop\ISE\Deep Learning\Challenge Task NLP 1 - Bug Localization\Dataset")
_SOURCE_ROOT = Path(r"E:\Desktop\ISE\Deep Learning\Challenge Task NLP 1 - Bug Localization\all_data_buglocalization\source files")
_BUG_REPORT_ROOT = Path(r"E:\Desktop\ISE\Deep Learning\Challenge Task NLP 1 - Bug Localization\all_data_buglocalization\bug reports")

Dataset = namedtuple('Dataset', ['name', 'src', 'bug_repo', 'repo_url', 'features'])
aspectj = Dataset(
    'aspectj',
    _SOURCE_ROOT / 'org.aspectj-bug433351/',
    _BUG_REPORT_ROOT / 'AspectJ.txt',
    "https://github.com/eclipse/org.aspectj/tree/bug433351.git",
    _DATASET_ROOT / 'features_aspectj.csv'
)

eclipse = Dataset(
    'eclipse',
    _SOURCE_ROOT / 'eclipse.platform.ui-johna-402445/',
    _BUG_REPORT_ROOT / 'Eclipse_Platform_UI.txt',
    "https://github.com/eclipse/eclipse.platform.ui.git",
    _DATASET_ROOT / 'features_eclipse.csv'
)

swt = Dataset(
    'swt',
    _SOURCE_ROOT / 'eclipse.platform.swt-xulrunner-31/',
    _BUG_REPORT_ROOT / 'SWT.txt',
    "https://github.com/eclipse/eclipse.platform.swt.git",
    _DATASET_ROOT / 'features_swt.csv'
)

tomcat = Dataset(
    'tomcat',
    _SOURCE_ROOT / 'tomcat-7.0.51/',
    _BUG_REPORT_ROOT / 'Tomcat.txt',
    "https://github.com/apache/tomcat.git",
    _DATASET_ROOT / 'features_tomcat/'
)

birt = Dataset(
    'birt',
    _SOURCE_ROOT / 'birt-20140211-1400/',
    _BUG_REPORT_ROOT / 'Birt.txt',
    "https://github.com/eclipse/birt.git",
    _DATASET_ROOT / 'features_birt.csv'
)

DATASET = aspectj

if __name__ == '__main__':
    print(DATASET.name, DATASET.src, DATASET.bug_repo)
