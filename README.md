Django는
Django는 파이썬으로 작성된 웹 프레임워크로, 웹 애플리케이션을 빠르고 효율적으로 개발할 수 있도록 다양한 기능을 제공한다.
2005년에 처음 공개된 Django는 "The web framework for perfectionists with deadlines"이라는 슬로건 아래 개발자 생산성을 극대화하는 데 초점이 맞춰져 있다.

Django의 주요 특징:
MTV 아키텍처: Model-Template-View 패턴을 기반으로 함.
완전한 패키지: 인증, 관리자 인터페이스, 데이터베이스 ORM(Object-Relational Mapping) 등 다양한 기능 내장.
보안 강화: XSS, CSRF, SQL Injection 등의 공격 방어 도구를 기본 제공.
확장 가능성: 모듈식 설계로 손쉽게 기능 확장이 가능.
풍부한 생태계: 다양한 써드파티 패키지와 커뮤니티 지원.


MTV 패턴
Django는 **MTV (Model-Template-View)**라는 디자인 패턴을 사용한다.
MTV는 웹 애플리케이션의 구성 요소를 나누어 효율적인 개발과 유지보수를 지원하는 방식이다.

1. Model
데이터베이스와의 상호작용을 담당.
데이터의 구조(스키마)를 정의하고, 데이터를 저장하거나 수정하는 역할.
Django의 ORM(Object-Relational Mapping)을 통해 데이터베이스를 직접적으로 다룰 필요 없이 Python 코드로 작업 가능.
2. Template
사용자 인터페이스(UI)를 담당.
HTML 파일에 Django의 템플릿 태그와 변수를 사용해 동적으로 데이터를 표시.
모델로부터 받은 데이터를 기반으로 사용자에게 보여질 화면을 생성.
3. View
애플리케이션의 비즈니스 로직을 담당.
요청(Request)을 받아서 필요한 데이터를 모델에서 가져오고, 적절한 템플릿과 데이터를 사용자에게 응답(Response)으로 전달.
Django의 View는 URL과 매핑되어 사용자의 요청을 처리함.
MTV 패턴의 흐름
사용자가 URL을 통해 요청을 보냄.
View가 요청을 처리하며 필요한 데이터를 Model에서 가져옴.
가져온 데이터를 Template에 전달하여 동적 HTML을 생성.
최종적으로 사용자에게 완성된 HTML 응답을 반환.
Django와 MTV 패턴의 장점
구조적 분리: 데이터, 로직, UI를 분리하여 유지보수성과 확장성이 뛰어남.
재사용성: 각각의 컴포넌트(Model, Template, View)가 독립적으로 재사용 가능.
생산성 향상: Django가 제공하는 강력한 기능들(ORM, Admin Interface 등)을 통해 빠른 개발 가능.
Django와 MTV 패턴은 현대적인 웹 애플리케이션 개발에서 효율성과 생산성을 제공하는 중요한 도구와 설계 방식이다.
