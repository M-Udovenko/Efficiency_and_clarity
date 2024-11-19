from factories.social_network_factory import FacebookFactory, LinkedInFactory


def main():
    fb_factory = FacebookFactory(login="cool_user", password="secret123")
    li_factory = LinkedInFactory(email="professional@email.com", password="work456")

    facebook = fb_factory.create_network()
    linkedin = li_factory.create_network()

    facebook.connect()
    linkedin.connect()

    message = "🚀 Изучаю паттерны проектирования! #coding #patterns"
    facebook.post_message(message)
    linkedin.post_message(message)

    facebook.disconnect()
    linkedin.disconnect()


if __name__ == "__main__":
    main()