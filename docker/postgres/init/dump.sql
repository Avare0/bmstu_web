
COPY public.api_app_cities (id, name, country_id) FROM stdin;
1	Москва	1
3	Париж	2
4	Нью-Йорк	3
5	Оттава	4
6	Прага	5
7	Рим	6
8	Берн	7
9	Нурсултан	8
10	Пекин	9
\.


--
-- Data for Name: api_app_countries; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_app_countries (id, name) FROM stdin;
1	Россия
2	Франция
3	США
4	Канада
5	Чехия
6	Италия
7	Швейцария
8	Казахстан
9	Китай
10	Япония
11	Англия
\.


--
-- Data for Name: api_app_facilities; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_app_facilities (id, name, file) FROM stdin;
1	Сауна	img/facilities/sauna.png
2	Бассейн	img/facilities/pool.png
3	Красивый вид	img/facilities/view.png
4	Стиральная машина	img/facilities/washing-machine.png
5	Парковка	img/facilities/parking.png
6	Кондиционер	img/facilities/conditioner.png
7	WI-FI	img/facilities/wifi.png
\.


--
-- Data for Name: api_app_house_facilities; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_app_house_facilities (id, facility_id, house_id) FROM stdin;
8	1	3
9	2	3
10	3	3
11	6	3
12	6	4
13	7	4
14	2	5
15	3	5
16	4	5
17	3	6
18	4	6
19	5	6
20	4	7
21	1	8
22	3	8
23	5	8
24	6	8
25	7	8
26	1	9
27	2	9
28	3	9
29	6	9
30	1	10
31	2	10
32	3	10
33	4	10
34	5	10
35	7	10
36	1	11
37	2	11
38	7	11
39	2	12
40	4	12
44	1	14
45	4	14
46	5	14
52	3	13
53	4	13
54	6	13
66	4	2
67	5	2
68	7	2
\.


--
-- Data for Name: api_app_house_photos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_app_house_photos (id, file, house_id) FROM stdin;
3	91adfb74078363.5c20be2c04a05_WGxxoNJ_aIb9W1F_Qe41DNw.jpg	2
4	1600948784_interior_74_PsZe3so_jLOcpRo_a9WbHKf.jpg	2
5	3d2a1b1d.jpeg	3
6	7c9fa844d9f840c09874a33b.jpeg	3
7	1606909189_3.jpeg	4
8	Image059.jpeg	4
9	wallperz.com_swovc7gskzxqp0vm6yysaj9pt8gax2.jpg	5
10	zbg-30-hvparisfrance.jpeg	5
11	interior-design-image-wallpaper-1920x1080-0106.jpeg	6
12	kvartira-dizajn-kuxnya-divan-stolik-televizor-lyustry.jpeg	6
13	7c9fa844d9f840c09874a33b_IxWEHMY.jpeg	7
14	1672-odnokomnatnaya_kvartira-nyu_jork-uslugi_dizajn_interera-nedvizhimost-kvartira-1920x1080.jpeg	7
15	1672-odnokomnatnaya_kvartira-nyu_jork-uslugi_dizajn_interera-nedvizhimost-kvartira-1920_IRTqX8O.jpeg	8
16	1606909189_3_qgH17Af.jpeg	8
17	3d2a1b1d_Y4F3vED.jpeg	9
18	interior-design-image-wallpaper-1920x1080-0106_5v2Vo4c.jpeg	9
19	1.jpeg	10
20	1606909189_3_kIfDyWJ.jpeg	10
21	vidovaya-kvartira.jpeg	11
22	zbg-30-hvparisfrance_gc6WaGx.jpeg	11
23	Image059_71go64b.jpeg	12
24	interior-design-image-wallpaper-1920x1080-0106_toO4gAL.jpeg	12
25	1_3n5225F.jpeg	13
26	interior-design-image-wallpaper-1920x1080-0106_jWVmJN1.jpeg	13
27	interior-design-image-wallpaper-1920x1080-0106_Oc0oKbp.jpeg	14
28	sofa-home-turquoise-sea.jpeg	14
\.


--
-- Data for Name: api_app_houses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_app_houses (id, name, "desc", guests_amount, beds_amount, address, rules, bathrooms_amount, city_id, owner_id) FROM stdin;
3	Апартаменты с красивым видом	В центре Рима с крутым видом	5	3	ул. Римская, д.3, кв.12	Владелец не указал особых правил проживания	1	7	3
4	Лучшие апартаменты в Берне	Прямо в центре столицы Швейцарии	6	5	ул. Швейцара, д.6, кв.123	Владелец не указал особых правил проживания	2	8	3
5	Уютная квартира с WIFI	Уютное местечко	4	4	ул. Академика Королева, д.5, кв.23	Не пить не курить не шуметь	1	10	3
6	Квартира прямо в центре Нью-Йорка	Вид на Эмпайр стейт билдинг	2	1	ул. Волл стрит, д.5, кв.12	Не устраивать вечеринки	2	4	3
7	Маленькая квартира в Нью-Йорке	Уютненькая маленькая квартирка	1	1	ул. Маяковская, д.3, кв.12	Не шуметь, вести себя тихо	1	4	4
8	Элитное жилье в Москве Сити	500 кв.м, сауна и бассейн	4	2	Москва Сити, башня Федерация, кв.34	Владелец не указал особых правил проживания	1	1	4
9	Апартаменты с красивым видом на море	Крутой вид	5	4	ул. Главная, д.2, кв.34	Не шуметь, не кушать, не пить воды	2	6	4
10	Дом на Рублевке	Элитная недвижимость, свой участок	10	6	Рублевское шоссе, д.3,	Не поджигать дом	5	1	4
11	Квартира в центре столицы Канады	Крутое жилье с прикольным видом	4	4	ул. Большая канадская, д.2, кв.54	Никаких вечеринок	2	5	4
12	Уютные апартаменты в центре Нурсултана	Красивый вид, добрые соседи	12	5	ул. Большая казахская, д.3, кв.67	Владелец не указал особых правил проживания	5	9	4
14	Квартира с видом на главную площадь	Красивый вид, уютная квартира	4	4	ул. Пражская, д.1, кв.56	Не устраивать вечеринки	12	6	4
2	Квартира в Париже	С видом на Эйфилеву Башню!	2	1	ул. Парижская, д.3, кв.1	Владелец не указал особых правил проживания	1	3	3
13	Крутая квартира в Пекине	Шаговая доступность до метро и хорошая отделка	4	3	ул. Пекинская, д.7, кв.12	Не шуметь	1	10	4
\.


--
-- Data for Name: api_app_messages; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_app_messages (id, message, date, from_user_id, to_user_id) FROM stdin;
1	Привет!	2021-10-02 03:07:19.596693+03	5	3
2	Здарова	2021-10-02 03:09:36.248124+03	6	3
3	Привет! Как дела?	2021-10-02 03:31:43.129216+03	1	6
4	Привет, отлично, у тя как?	2021-10-02 03:32:07.239511+03	6	1
5	Че делаешь?	2021-10-02 10:47:42.472525+03	1	6
6	Как попасть в ваш дом?	2021-10-02 10:48:09.048383+03	5	3
\.


--
-- Data for Name: api_app_orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_app_orders (id, date_from, date_till, date, guests_amount, house_id, user_id) FROM stdin;
3	2021-10-08	2021-10-22	2021-10-02	2	2	1
4	2021-10-09	2021-10-23	2021-10-02	6	12	5
\.


--
-- Data for Name: api_app_testimonials; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_app_testimonials (id, text, date, house_id, user_id) FROM stdin;
6	Спасибо огромное хозяину!	2021-10-02	12	5
\.


--
-- Data for Name: api_app_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_app_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, sex, type, photo, city_id) FROM stdin;
3	pbkdf2_sha256$260000$CFVIUvf4HPqkBJjyRbB4IL$/RBAKMKeahsBvnAX1SvlRud2vxUkagW+c6URVVLkB1k=	2021-10-02 02:21:21.408406+03	f	owner	Маша	Светлова		f	t	2021-10-02 02:21:13.921859+03	f	owner	db_cw/files/media/lilo-and-stitch_70EPAuK.jpg	1
4	pbkdf2_sha256$260000$KsvIxcWxrtVCZ4Kh6wgsA1$yMuggdxYGCeb5zEZJorJd1kX3jU24oqBOYpoCl9bB6s=	2021-10-02 02:32:15.942906+03	f	owner2	Гена	Петров		f	t	2021-10-02 02:32:10.400382+03	m	owner	db_cw/files/media/avatar1.jpeg	5
2	pbkdf2_sha256$260000$krAX6zhWtvaCmAMdsovjgy$X4NQk5OfqrSW8zvZc6rKWuolGn610Rv7sxOd1RWIqoA=	2021-10-02 03:03:46.526095+03	f	guest	Василий	Макаров		f	t	2021-10-02 02:20:22.962286+03	m	guest	db_cw/files/media/unnamed_0EwUUXT.jpeg	1
6	pbkdf2_sha256$260000$Wha5xfjuyJln9szVkYAW3P$4YfL47alotglivB2GUl5vz7iglD+Jm6EjgxBk4BLAI8=	2021-10-02 03:31:56.390037+03	f	owner10	Геннадий	Макаров		f	t	2021-10-02 03:09:03.631807+03	m	owner	db_cw/files/media/avatar5.jpeg	9
1	pbkdf2_sha256$260000$2W4rOgwqBBcybDOJp21VoB$q+ZPuaFsbcsHpc4uM9XOyEIteiIMRSE9JfDTSflZUwI=	2021-10-02 03:41:42.207673+03	t	admin	Егор	Панафидин	admin@gmail.com	t	t	2021-10-02 02:19:47.763178+03	m	admin	db_cw/files/media/unnamed_0EwUUXT.jpeg	1
5	pbkdf2_sha256$260000$rybSFp8bJ0aGV1S5Wy47rF$hU6/MBLojcvj7uzqiARtegGYM90NhcWUPRopoX7ah64=	2021-10-02 10:47:57.748848+03	f	guest10	Света	Иванова		f	t	2021-10-02 03:06:47.221128+03	f	guest	db_cw/files/media/avatar3.jpeg	5
\.


--
-- Data for Name: api_app_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_app_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: api_app_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.api_app_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 60, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 15, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 19, true);


--
-- Name: api_app_cities_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_cities_id_seq', 1, false);


--
-- Name: api_app_countries_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_countries_id_seq', 1, false);


--
-- Name: api_app_facilities_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_facilities_id_seq', 1, false);


--
-- Name: api_app_house_facilities_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_house_facilities_id_seq', 68, true);


--
-- Name: api_app_house_photos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_house_photos_id_seq', 33, true);


--
-- Name: api_app_houses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_houses_id_seq', 16, true);


--
-- Name: api_app_messages_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_messages_id_seq', 6, true);


--
-- Name: api_app_orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_orders_id_seq', 4, true);


--
-- Name: api_app_testimonials_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_testimonials_id_seq', 7, true);


--
-- Name: api_app_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_user_groups_id_seq', 1, false);


--
-- Name: api_app_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_user_id_seq', 6, true);


--
-- Name: api_app_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_user_user_permissions_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: api_app_cities api_app_cities_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_cities
    ADD CONSTRAINT api_app_cities_pkey PRIMARY KEY (id);


--
-- Name: api_app_countries api_app_countries_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_countries
    ADD CONSTRAINT api_app_countries_pkey PRIMARY KEY (id);


--
-- Name: api_app_facilities api_app_facilities_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_facilities
    ADD CONSTRAINT api_app_facilities_pkey PRIMARY KEY (id);


--
-- Name: api_app_house_facilities api_app_house_facilities_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_house_facilities
    ADD CONSTRAINT api_app_house_facilities_pkey PRIMARY KEY (id);


--
-- Name: api_app_house_photos api_app_house_photos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_house_photos
    ADD CONSTRAINT api_app_house_photos_pkey PRIMARY KEY (id);


--
-- Name: api_app_houses api_app_houses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_houses
    ADD CONSTRAINT api_app_houses_pkey PRIMARY KEY (id);


--
-- Name: api_app_messages api_app_messages_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_messages
    ADD CONSTRAINT api_app_messages_pkey PRIMARY KEY (id);


--
-- Name: api_app_orders api_app_orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_orders
    ADD CONSTRAINT api_app_orders_pkey PRIMARY KEY (id);


--
-- Name: api_app_testimonials api_app_testimonials_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_testimonials
    ADD CONSTRAINT api_app_testimonials_pkey PRIMARY KEY (id);


--
-- Name: api_app_user_groups api_app_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user_groups
    ADD CONSTRAINT api_app_user_groups_pkey PRIMARY KEY (id);


--
-- Name: api_app_user_groups api_app_user_groups_user_id_group_id_ae195797_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user_groups
    ADD CONSTRAINT api_app_user_groups_user_id_group_id_ae195797_uniq UNIQUE (user_id, group_id);


--
-- Name: api_app_user api_app_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user
    ADD CONSTRAINT api_app_user_pkey PRIMARY KEY (id);


--
-- Name: api_app_user_user_permissions api_app_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user_user_permissions
    ADD CONSTRAINT api_app_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: api_app_user_user_permissions api_app_user_user_permissions_user_id_permission_id_96b9fadf_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user_user_permissions
    ADD CONSTRAINT api_app_user_user_permissions_user_id_permission_id_96b9fadf_uniq UNIQUE (user_id, permission_id);


--
-- Name: api_app_user api_app_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user
    ADD CONSTRAINT api_app_user_username_key UNIQUE (username);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: api_app_cities_country_id_c04bc0eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_cities_country_id_c04bc0eb ON public.api_app_cities USING btree (country_id);


--
-- Name: api_app_house_facilities_facility_id_0784ba6c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_house_facilities_facility_id_0784ba6c ON public.api_app_house_facilities USING btree (facility_id);


--
-- Name: api_app_house_facilities_house_id_11fbc10f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_house_facilities_house_id_11fbc10f ON public.api_app_house_facilities USING btree (house_id);


--
-- Name: api_app_house_photos_house_id_5908f7c6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_house_photos_house_id_5908f7c6 ON public.api_app_house_photos USING btree (house_id);


--
-- Name: api_app_houses_city_id_a01bb424; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_houses_city_id_a01bb424 ON public.api_app_houses USING btree (city_id);


--
-- Name: api_app_houses_owner_id_3f214655; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_houses_owner_id_3f214655 ON public.api_app_houses USING btree (owner_id);


--
-- Name: api_app_messages_from_user_id_c4ecda3e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_messages_from_user_id_c4ecda3e ON public.api_app_messages USING btree (from_user_id);


--
-- Name: api_app_messages_to_user_id_434cbaf7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_messages_to_user_id_434cbaf7 ON public.api_app_messages USING btree (to_user_id);


--
-- Name: api_app_orders_house_id_9de8707d; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_orders_house_id_9de8707d ON public.api_app_orders USING btree (house_id);


--
-- Name: api_app_orders_user_id_7dcceb21; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_orders_user_id_7dcceb21 ON public.api_app_orders USING btree (user_id);


--
-- Name: api_app_testimonials_house_id_47151b51; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_testimonials_house_id_47151b51 ON public.api_app_testimonials USING btree (house_id);


--
-- Name: api_app_testimonials_user_id_8e782108; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_testimonials_user_id_8e782108 ON public.api_app_testimonials USING btree (user_id);


--
-- Name: api_app_user_city_id_67955cf3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_user_city_id_67955cf3 ON public.api_app_user USING btree (city_id);


--
-- Name: api_app_user_groups_group_id_a337ba62; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_user_groups_group_id_a337ba62 ON public.api_app_user_groups USING btree (group_id);


--
-- Name: api_app_user_groups_user_id_df502602; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_user_groups_user_id_df502602 ON public.api_app_user_groups USING btree (user_id);


--
-- Name: api_app_user_user_permissions_permission_id_cd2b56a3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_user_user_permissions_permission_id_cd2b56a3 ON public.api_app_user_user_permissions USING btree (permission_id);


--
-- Name: api_app_user_user_permissions_user_id_451ce57f; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_user_user_permissions_user_id_451ce57f ON public.api_app_user_user_permissions USING btree (user_id);


--
-- Name: api_app_user_username_6330637b_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_user_username_6330637b_like ON public.api_app_user USING btree (username varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_api_app_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_api_app_user_id FOREIGN KEY (user_id) REFERENCES public.api_app_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_cities api_app_cities_country_id_c04bc0eb_fk_api_app_countries_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_cities
    ADD CONSTRAINT api_app_cities_country_id_c04bc0eb_fk_api_app_countries_id FOREIGN KEY (country_id) REFERENCES public.api_app_countries(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_house_facilities api_app_house_facilitie_facility_id_0784ba6c_fk_api_app_faci; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_house_facilities
    ADD CONSTRAINT api_app_house_facilitie_facility_id_0784ba6c_fk_api_app_faci FOREIGN KEY (facility_id) REFERENCES public.api_app_facilities(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_house_facilities api_app_house_facilities_house_id_11fbc10f_fk_api_app_houses_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_house_facilities
    ADD CONSTRAINT api_app_house_facilities_house_id_11fbc10f_fk_api_app_houses_id FOREIGN KEY (house_id) REFERENCES public.api_app_houses(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_house_photos api_app_house_photos_house_id_5908f7c6_fk_api_app_houses_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_house_photos
    ADD CONSTRAINT api_app_house_photos_house_id_5908f7c6_fk_api_app_houses_id FOREIGN KEY (house_id) REFERENCES public.api_app_houses(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_houses api_app_houses_city_id_a01bb424_fk_api_app_cities_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_houses
    ADD CONSTRAINT api_app_houses_city_id_a01bb424_fk_api_app_cities_id FOREIGN KEY (city_id) REFERENCES public.api_app_cities(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_houses api_app_houses_owner_id_3f214655_fk_api_app_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_houses
    ADD CONSTRAINT api_app_houses_owner_id_3f214655_fk_api_app_user_id FOREIGN KEY (owner_id) REFERENCES public.api_app_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_messages api_app_messages_from_user_id_c4ecda3e_fk_api_app_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_messages
    ADD CONSTRAINT api_app_messages_from_user_id_c4ecda3e_fk_api_app_user_id FOREIGN KEY (from_user_id) REFERENCES public.api_app_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_messages api_app_messages_to_user_id_434cbaf7_fk_api_app_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_messages
    ADD CONSTRAINT api_app_messages_to_user_id_434cbaf7_fk_api_app_user_id FOREIGN KEY (to_user_id) REFERENCES public.api_app_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_orders api_app_orders_house_id_9de8707d_fk_api_app_houses_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_orders
    ADD CONSTRAINT api_app_orders_house_id_9de8707d_fk_api_app_houses_id FOREIGN KEY (house_id) REFERENCES public.api_app_houses(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_orders api_app_orders_user_id_7dcceb21_fk_api_app_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_orders
    ADD CONSTRAINT api_app_orders_user_id_7dcceb21_fk_api_app_user_id FOREIGN KEY (user_id) REFERENCES public.api_app_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_testimonials api_app_testimonials_house_id_47151b51_fk_api_app_houses_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_testimonials
    ADD CONSTRAINT api_app_testimonials_house_id_47151b51_fk_api_app_houses_id FOREIGN KEY (house_id) REFERENCES public.api_app_houses(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_testimonials api_app_testimonials_user_id_8e782108_fk_api_app_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_testimonials
    ADD CONSTRAINT api_app_testimonials_user_id_8e782108_fk_api_app_user_id FOREIGN KEY (user_id) REFERENCES public.api_app_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_user api_app_user_city_id_67955cf3_fk_api_app_cities_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user
    ADD CONSTRAINT api_app_user_city_id_67955cf3_fk_api_app_cities_id FOREIGN KEY (city_id) REFERENCES public.api_app_cities(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_user_groups api_app_user_groups_group_id_a337ba62_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user_groups
    ADD CONSTRAINT api_app_user_groups_group_id_a337ba62_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_user_groups api_app_user_groups_user_id_df502602_fk_api_app_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user_groups
    ADD CONSTRAINT api_app_user_groups_user_id_df502602_fk_api_app_user_id FOREIGN KEY (user_id) REFERENCES public.api_app_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_user_user_permissions api_app_user_user_permi_permission_id_cd2b56a3_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user_user_permissions
    ADD CONSTRAINT api_app_user_user_permi_permission_id_cd2b56a3_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_user_user_permissions api_app_user_user_permissions_user_id_451ce57f_fk_api_app_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user_user_permissions
    ADD CONSTRAINT api_app_user_user_permissions_user_id_451ce57f_fk_api_app_user_id FOREIGN KEY (user_id) REFERENCES public.api_app_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

