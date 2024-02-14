# keyword-jinja-fastapi

[![PyPI - Version](https://img.shields.io/pypi/v/jinja2-fastapi-users.svg)](https://pypi.org/project/jinja2-fastapi-users)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jinja2-fastapi-users.svg)](https://pypi.org/project/jinja2-fastapi-users)

-----

**Table of Contents**

- [Overview](#overview)
- [Installation](#installation)
- [License](#license)
- [How to use](#how-to-use)
- [tech stack](#tech-stack)


## Overview
- 콘텐츠의 키워드 설정 작업을 할 때 시리즈, 같은 작품, 다른 버전 등 유사한 콘텐츠의 키워드를 복사해서 작업시간의 효율성을 높입니다.
- 복사한 키워드는 로그 페이지를 통해서 확인할 수 있다.
- 모놀리스 애플리케이션으로 FE-BE 구성없이 FASTAPI+JINJA2를 활용해 간단하고 빠르게 구현 한 앱입니다.


## Installation

```console
copy dotenv                         # 환경변수 파일 복사/삽입
hatch init                          # hatch 초기화
hatch shell                         # hatch 실행
pip install -r requirements.txt     # 패키지 설치
hatch run dev                       # 개발 서버 실행
``````


## How to use

1. 컨텐츠 키워드 복사는 왼쪽에서 오른쪽으로 이루어진다.
2. 왼쪽에 원본 컨텐츠를 불러온다. 섬네일 이미지로 컨텐츠를 확인한다.
3. 오른쪽에 목표 컨텐츠를 불러온다. 섬네일 이미지로 컨텐츠를 확인한다.
4. 중앙의 copy 버튼을 눌러 키워드를 복사한다. (단축키: ctrl + alt + c)
5. Log page를 통해서 복사 내역을 확인 할 수 있다.


## tech stack

- python
- hatch : project manager
- fastapi : backend framework
- jinja2 : view template
- sqlalchemy + aioodbc : mssql async orm


## License

`keyword-jinja-fastapi` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
