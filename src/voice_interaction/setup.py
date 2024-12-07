from setuptools import setup
from setuptools import find_packages  # 패키지 자동 검색을 위해 추가

package_name = "voice_interaction"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),  # 패키지 자동 검색
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="root",
    maintainer_email="eddie36@naver.com",
    description="Voice command package for ROS2 dog robot",  # 구체적인 설명 추가
    license="Apache License 2.0",  # 라이선스 명시
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "dog_behavior_server = voice_interaction.dog_behavior_server:main",
            "interaction_client = voice_interaction.interaction_client:main",
        ],
    },
    python_requires=">=3.6",  # Python 버전 요구사항 추가
)
