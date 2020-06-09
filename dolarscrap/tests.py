from datetime import datetime
from decimal import Decimal

import pytest
from freezegun import freeze_time

from django.urls import reverse

from dolarscrap.models import Dollar, Type


def test_dollar_average():
    # 1 - construir el entorno
    dollar = Dollar()
    dollar.buy_price = Decimal('55.54')
    dollar.sell_price = Decimal('54.14')

    # 2 - ejecución
    avg = dollar.average()

    # 3 - comparación
    assert avg == Decimal('54.84')


@freeze_time("2020-5-1")
def test_is_not_today_method():
    dollar = Dollar()
    dollar.issue_date = datetime(2020, 3, 24)

    assert not dollar.is_today()


@freeze_time("2020-5-1")
def test_is_today_method():
    dollar = Dollar()
    dollar.issue_date = datetime(2020, 5, 1)

    assert dollar.is_today()


@pytest.mark.django_db
def test_index_view_200(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_index_view_show_list(client):
    today = datetime.today()
    type1 = Type.objects.create(name='oficial')
    dollar1 = Dollar.objects.create(origin='dolarhoy', dollar_type=type1, issue_date=today, buy_price=66, sell_price=64)
    dollar2 = Dollar.objects.create(origin='lanacion', dollar_type=type1, issue_date=today, buy_price=67, sell_price=63)

    url = reverse('index')
    response = client.get(url)

    assert response.status_code == 200

    assert dollar1 in response.context['dollars']
    assert dollar2 in response.context['dollars']
    assert 'dolarscrap/dollar_list.html' == response.templates[0].name
