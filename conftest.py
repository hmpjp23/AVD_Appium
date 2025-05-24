import pytest
from utils.driver_factory import DriverFactory

@pytest.fixture(scope="function")
def driver():
    """
    각 테스트 함수마다 새로운 드라이버 인스턴스를 생성합니다.
    """

    # 테스트 실핼 전 : 드라이버 생성 
    driver = DriverFactory.get_driver()
    yield driver
    # 테스트 실행 후 : 드라이버 종료 
    driver.quit()
