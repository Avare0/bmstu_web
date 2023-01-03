from .BaseRepository import BaseRepository
from ..models import Orders
class OrdersRepository(BaseRepository):
    model = Orders

    def check_availiable_date(self, dt_from, dt_till, house_id):
        orders = self.sql(
            f"""
            select * from api_app_orders
            where ('{dt_from}'::date between date_from and date_till
            or '{dt_till}'::date between date_from and date_till
            or '{dt_from}'::date < date_from and date_till < '{dt_till}'::date) and house_id = {house_id}
            """
        )
        return len(orders) == 0 and dt_from <= dt_till

