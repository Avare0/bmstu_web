from ..repositories.TestimonialsRepository import *

class TestimonialBuilder:
    def __init__(self):
        self.rep = TestimonialsRepository()

        self.testimonial = Testimonials()

    def with_house(self, id):
        self.testimonial.house_id = id
        return self

    def with_date(self, date):
        self.testimonial.date = date
        return self

    def with_user(self, id):
        self.testimonial.user_id = id
        return self

    def with_text(self, text):
        self.testimonial.text = text
        return self

    def build(self):
        return self.rep.create(text=self.testimonial.text,
                               date=self.testimonial.date,
                               house=self.testimonial.house,
                               user=self.testimonial.user)
