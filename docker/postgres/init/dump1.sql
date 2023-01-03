--
-- PostgreSQL database dump
--

-- Dumped from database version 12.8 (Debian 12.8-1.pgdg110+1)
-- Dumped by pg_dump version 14.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: airbnb; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE airbnb WITH TEMPLATE = template0 ENCODING = 'UTF8';


ALTER DATABASE airbnb OWNER TO postgres;

\connect airbnb

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: api_app_cities; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_app_cities (
	id bigint NOT NULL,
	name character varying(50) NOT NULL,
	country_id bigint
);


ALTER TABLE public.api_app_cities OWNER TO postgres;

--
-- Name: api_app_cities_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_app_cities_id_seq
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.api_app_cities_id_seq OWNER TO postgres;

--
-- Name: api_app_cities_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_app_cities_id_seq OWNED BY public.api_app_cities.id;


--
-- Name: api_app_countries; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_app_countries (
	id bigint NOT NULL,
	name character varying(50) NOT NULL
);


ALTER TABLE public.api_app_countries OWNER TO postgres;

--
-- Name: api_app_countries_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_app_countries_id_seq
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.api_app_countries_id_seq OWNER TO postgres;

--
-- Name: api_app_countries_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_app_countries_id_seq OWNED BY public.api_app_countries.id;


--
-- Name: api_app_facilities; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_app_facilities (
	id bigint NOT NULL,
	name character varying(50) NOT NULL,
	file character varying(100) NOT NULL
);


ALTER TABLE public.api_app_facilities OWNER TO postgres;

--
-- Name: api_app_facilities_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_app_facilities_id_seq
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.api_app_facilities_id_seq OWNER TO postgres;

--
-- Name: api_app_facilities_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_app_facilities_id_seq OWNED BY public.api_app_facilities.id;


--
-- Name: api_app_house_facilities; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_app_house_facilities (
	id bigint NOT NULL,
	facility_id bigint NOT NULL,
	house_id bigint NOT NULL
);


ALTER TABLE public.api_app_house_facilities OWNER TO postgres;

--
-- Name: api_app_house_facilities_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_app_house_facilities_id_seq
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.api_app_house_facilities_id_seq OWNER TO postgres;

--
-- Name: api_app_house_facilities_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_app_house_facilities_id_seq OWNED BY public.api_app_house_facilities.id;


--
-- Name: api_app_house_photos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_app_house_photos (
	id bigint NOT NULL,
	photo character varying(100) NOT NULL,
	house_id bigint
);


ALTER TABLE public.api_app_house_photos OWNER TO postgres;

--
-- Name: api_app_house_photos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_app_house_photos_id_seq
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.api_app_house_photos_id_seq OWNER TO postgres;

--
-- Name: api_app_house_photos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_app_house_photos_id_seq OWNED BY public.api_app_house_photos.id;


--
-- Name: api_app_houses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_app_houses (
	id bigint NOT NULL,
	name character varying(50) NOT NULL,
	"desc" text NOT NULL,
	guests_amount integer NOT NULL,
	beds_amount integer NOT NULL,
	address character varying(100) NOT NULL,
	rules text NOT NULL,
	bathrooms_amount integer NOT NULL,
	city_id bigint,
	owner_id bigint
);


ALTER TABLE public.api_app_houses OWNER TO postgres;

--
-- Name: api_app_houses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_app_houses_id_seq
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.api_app_houses_id_seq OWNER TO postgres;

--
-- Name: api_app_houses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_app_houses_id_seq OWNED BY public.api_app_houses.id;


--
-- Name: api_app_messages; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_app_messages (
	id bigint NOT NULL,
	message text NOT NULL,
	date timestamp with time zone NOT NULL,
	from_user_id bigint NOT NULL,
	to_user_id bigint NOT NULL
);


ALTER TABLE public.api_app_messages OWNER TO postgres;

--
-- Name: api_app_messages_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_app_messages_id_seq
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.api_app_messages_id_seq OWNER TO postgres;

--
-- Name: api_app_messages_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_app_messages_id_seq OWNED BY public.api_app_messages.id;


--
-- Name: api_app_orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_app_orders (
	id bigint NOT NULL,
	date_from date NOT NULL,
	date_till date NOT NULL,
	date date NOT NULL,
	guests_amount integer,
	house_id bigint,
	user_id bigint
);


ALTER TABLE public.api_app_orders OWNER TO postgres;

--
-- Name: api_app_orders_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_app_orders_id_seq
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.api_app_orders_id_seq OWNER TO postgres;

--
-- Name: api_app_orders_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_app_orders_id_seq OWNED BY public.api_app_orders.id;


--
-- Name: api_app_testimonials; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_app_testimonials (
	id bigint NOT NULL,
	text text NOT NULL,
	date date,
	house_id bigint,
	user_id bigint
);


ALTER TABLE public.api_app_testimonials OWNER TO postgres;

--
-- Name: api_app_testimonials_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_app_testimonials_id_seq
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.api_app_testimonials_id_seq OWNER TO postgres;

--
-- Name: api_app_testimonials_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_app_testimonials_id_seq OWNED BY public.api_app_testimonials.id;


--
-- Name: api_app_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_app_user (
	id bigint NOT NULL,
	password character varying(128) NOT NULL,
	last_login timestamp with time zone,
	is_superuser boolean NOT NULL,
	username character varying(150) NOT NULL,
	first_name character varying(150) NOT NULL,
	last_name character varying(150) NOT NULL,
	email character varying(254) NOT NULL,
	is_staff boolean NOT NULL,
	is_active boolean NOT NULL,
	date_joined timestamp with time zone NOT NULL,
	sex character varying(1) NOT NULL,
	type character varying(7) NOT NULL,
	photo character varying(100) NOT NULL,
	city_id bigint NOT NULL
);


ALTER TABLE public.api_app_user OWNER TO postgres;

--
-- Name: api_app_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_app_user_groups (
	id bigint NOT NULL,
	user_id bigint NOT NULL,
	group_id integer NOT NULL
);


ALTER TABLE public.api_app_user_groups OWNER TO postgres;

--
-- Name: api_app_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_app_user_groups_id_seq
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.api_app_user_groups_id_seq OWNER TO postgres;

--
-- Name: api_app_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_app_user_groups_id_seq OWNED BY public.api_app_user_groups.id;


--
-- Name: api_app_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_app_user_id_seq
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.api_app_user_id_seq OWNER TO postgres;

--
-- Name: api_app_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_app_user_id_seq OWNED BY public.api_app_user.id;


--
-- Name: api_app_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.api_app_user_user_permissions (
	id bigint NOT NULL,
	user_id bigint NOT NULL,
	permission_id integer NOT NULL
);


ALTER TABLE public.api_app_user_user_permissions OWNER TO postgres;

--
-- Name: api_app_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.api_app_user_user_permissions_id_seq
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.api_app_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: api_app_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.api_app_user_user_permissions_id_seq OWNED BY public.api_app_user_user_permissions.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
	id integer NOT NULL,
	name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
	AS integer
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
	id bigint NOT NULL,
	group_id integer NOT NULL,
	permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
	id integer NOT NULL,
	name character varying(255) NOT NULL,
	content_type_id integer NOT NULL,
	codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
	AS integer
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
	id integer NOT NULL,
	action_time timestamp with time zone NOT NULL,
	object_id text,
	object_repr character varying(200) NOT NULL,
	action_flag smallint NOT NULL,
	change_message text NOT NULL,
	content_type_id integer,
	user_id bigint NOT NULL,
	CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
	AS integer
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
	id integer NOT NULL,
	app_label character varying(100) NOT NULL,
	model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
	AS integer
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
	id bigint NOT NULL,
	app character varying(255) NOT NULL,
	name character varying(255) NOT NULL,
	applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
	START WITH 1
	INCREMENT BY 1
	NO MINVALUE
	NO MAXVALUE
	CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
	session_key character varying(40) NOT NULL,
	session_data text NOT NULL,
	expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: api_app_cities id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_cities ALTER COLUMN id SET DEFAULT nextval('public.api_app_cities_id_seq'::regclass);


--
-- Name: api_app_countries id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_countries ALTER COLUMN id SET DEFAULT nextval('public.api_app_countries_id_seq'::regclass);


--
-- Name: api_app_facilities id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_facilities ALTER COLUMN id SET DEFAULT nextval('public.api_app_facilities_id_seq'::regclass);


--
-- Name: api_app_house_facilities id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_house_facilities ALTER COLUMN id SET DEFAULT nextval('public.api_app_house_facilities_id_seq'::regclass);


--
-- Name: api_app_house_photos id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_house_photos ALTER COLUMN id SET DEFAULT nextval('public.api_app_house_photos_id_seq'::regclass);


--
-- Name: api_app_houses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_houses ALTER COLUMN id SET DEFAULT nextval('public.api_app_houses_id_seq'::regclass);


--
-- Name: api_app_messages id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_messages ALTER COLUMN id SET DEFAULT nextval('public.api_app_messages_id_seq'::regclass);


--
-- Name: api_app_orders id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_orders ALTER COLUMN id SET DEFAULT nextval('public.api_app_orders_id_seq'::regclass);


--
-- Name: api_app_testimonials id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_testimonials ALTER COLUMN id SET DEFAULT nextval('public.api_app_testimonials_id_seq'::regclass);


--
-- Name: api_app_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user ALTER COLUMN id SET DEFAULT nextval('public.api_app_user_id_seq'::regclass);


--
-- Name: api_app_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user_groups ALTER COLUMN id SET DEFAULT nextval('public.api_app_user_groups_id_seq'::regclass);


--
-- Name: api_app_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.api_app_user_user_permissions_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: api_app_cities; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: api_app_countries; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: api_app_facilities; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: api_app_house_facilities; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: api_app_house_photos; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: api_app_houses; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: api_app_messages; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: api_app_orders; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: api_app_testimonials; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: api_app_user; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: api_app_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: api_app_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (21, 'Can add user', 6, 'add_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (22, 'Can change user', 6, 'change_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (23, 'Can delete user', 6, 'delete_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (24, 'Can view user', 6, 'view_user');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (25, 'Can add cities', 7, 'add_cities');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (26, 'Can change cities', 7, 'change_cities');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (27, 'Can delete cities', 7, 'delete_cities');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (28, 'Can view cities', 7, 'view_cities');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (29, 'Can add countries', 8, 'add_countries');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (30, 'Can change countries', 8, 'change_countries');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (31, 'Can delete countries', 8, 'delete_countries');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (32, 'Can view countries', 8, 'view_countries');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (33, 'Can add facilities', 9, 'add_facilities');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (34, 'Can change facilities', 9, 'change_facilities');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (35, 'Can delete facilities', 9, 'delete_facilities');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (36, 'Can view facilities', 9, 'view_facilities');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (37, 'Can add houses', 10, 'add_houses');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (38, 'Can change houses', 10, 'change_houses');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (39, 'Can delete houses', 10, 'delete_houses');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (40, 'Can view houses', 10, 'view_houses');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (41, 'Can add testimonials', 11, 'add_testimonials');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (42, 'Can change testimonials', 11, 'change_testimonials');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (43, 'Can delete testimonials', 11, 'delete_testimonials');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (44, 'Can view testimonials', 11, 'view_testimonials');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (45, 'Can add orders', 12, 'add_orders');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (46, 'Can change orders', 12, 'change_orders');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (47, 'Can delete orders', 12, 'delete_orders');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (48, 'Can view orders', 12, 'view_orders');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (49, 'Can add messages', 13, 'add_messages');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (50, 'Can change messages', 13, 'change_messages');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (51, 'Can delete messages', 13, 'delete_messages');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (52, 'Can view messages', 13, 'view_messages');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (53, 'Can add house_photos', 14, 'add_house_photos');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (54, 'Can change house_photos', 14, 'change_house_photos');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (55, 'Can delete house_photos', 14, 'delete_house_photos');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (56, 'Can view house_photos', 14, 'view_house_photos');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (57, 'Can add house_ facilities', 15, 'add_house_facilities');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (58, 'Can change house_ facilities', 15, 'change_house_facilities');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (59, 'Can delete house_ facilities', 15, 'delete_house_facilities');
INSERT INTO public.auth_permission (id, name, content_type_id, codename) VALUES (60, 'Can view house_ facilities', 15, 'view_house_facilities');


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_content_type (id, app_label, model) VALUES (1, 'admin', 'logentry');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (2, 'auth', 'permission');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (3, 'auth', 'group');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (5, 'sessions', 'session');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (6, 'api_app', 'user');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (7, 'api_app', 'cities');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (8, 'api_app', 'countries');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (9, 'api_app', 'facilities');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (10, 'api_app', 'houses');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (11, 'api_app', 'testimonials');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (12, 'api_app', 'orders');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (13, 'api_app', 'messages');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (14, 'api_app', 'house_photos');
INSERT INTO public.django_content_type (id, app_label, model) VALUES (15, 'api_app', 'house_facilities');


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.django_migrations (id, app, name, applied) VALUES (1, 'contenttypes', '0001_initial', '2021-10-30 16:38:04.87235+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (2, 'contenttypes', '0002_remove_content_type_name', '2021-10-30 16:38:04.984074+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (3, 'auth', '0001_initial', '2021-10-30 16:38:05.556655+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (4, 'auth', '0002_alter_permission_name_max_length', '2021-10-30 16:38:05.629068+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (5, 'auth', '0003_alter_user_email_max_length', '2021-10-30 16:38:05.672027+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (6, 'auth', '0004_alter_user_username_opts', '2021-10-30 16:38:05.697011+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (7, 'auth', '0005_alter_user_last_login_null', '2021-10-30 16:38:05.738729+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (8, 'auth', '0006_require_contenttypes_0002', '2021-10-30 16:38:05.78077+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (9, 'auth', '0007_alter_validators_add_error_messages', '2021-10-30 16:38:05.818431+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (10, 'auth', '0008_alter_user_username_max_length', '2021-10-30 16:38:05.844843+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (11, 'auth', '0009_alter_user_last_name_max_length', '2021-10-30 16:38:05.918082+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (12, 'auth', '0010_alter_group_name_max_length', '2021-10-30 16:38:05.97981+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (13, 'auth', '0011_update_proxy_permissions', '2021-10-30 16:38:06.01363+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (14, 'auth', '0012_alter_user_first_name_max_length', '2021-10-30 16:38:06.050683+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (15, 'api_app', '0001_initial', '2021-10-30 16:38:08.563653+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (16, 'admin', '0001_initial', '2021-10-30 16:38:08.736578+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (17, 'admin', '0002_logentry_remove_auto_add', '2021-10-30 16:38:08.760176+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (18, 'admin', '0003_logentry_add_action_flag_choices', '2021-10-30 16:38:08.799803+00');
INSERT INTO public.django_migrations (id, app, name, applied) VALUES (19, 'sessions', '0001_initial', '2021-10-30 16:38:08.930292+00');


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--



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

SELECT pg_catalog.setval('public.api_app_house_facilities_id_seq', 1, false);


--
-- Name: api_app_house_photos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_house_photos_id_seq', 1, false);


--
-- Name: api_app_houses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_houses_id_seq', 1, false);


--
-- Name: api_app_messages_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_messages_id_seq', 1, false);


--
-- Name: api_app_orders_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_orders_id_seq', 1, false);


--
-- Name: api_app_testimonials_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_testimonials_id_seq', 1, false);


--
-- Name: api_app_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_user_groups_id_seq', 1, false);


--
-- Name: api_app_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_user_id_seq', 1, false);


--
-- Name: api_app_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.api_app_user_user_permissions_id_seq', 1, false);


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
-- Name: api_app_user_groups api_app_user_groups_user_id_group_id_1888778b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user_groups
	ADD CONSTRAINT api_app_user_groups_user_id_group_id_1888778b_uniq UNIQUE (user_id, group_id);


--
-- Name: api_app_user api_app_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user
	ADD CONSTRAINT api_app_user_pkey PRIMARY KEY (id);


--
-- Name: api_app_user_user_permissions api_app_user_user_permis_user_id_permission_id_5ff28959_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user_user_permissions
	ADD CONSTRAINT api_app_user_user_permis_user_id_permission_id_5ff28959_uniq UNIQUE (user_id, permission_id);


--
-- Name: api_app_user_user_permissions api_app_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user_user_permissions
	ADD CONSTRAINT api_app_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: api_app_user api_app_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user
	ADD CONSTRAINT api_app_user_username_key UNIQUE (username);


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
-- Name: api_app_cities_country_id_6ac39f3b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_cities_country_id_6ac39f3b ON public.api_app_cities USING btree (country_id);


--
-- Name: api_app_house_facilities_facility_id_c3df75b1; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_house_facilities_facility_id_c3df75b1 ON public.api_app_house_facilities USING btree (facility_id);


--
-- Name: api_app_house_facilities_house_id_b43f1271; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_house_facilities_house_id_b43f1271 ON public.api_app_house_facilities USING btree (house_id);


--
-- Name: api_app_house_photos_house_id_ac6edd9e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_house_photos_house_id_ac6edd9e ON public.api_app_house_photos USING btree (house_id);


--
-- Name: api_app_houses_city_id_0a2f69c4; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_houses_city_id_0a2f69c4 ON public.api_app_houses USING btree (city_id);


--
-- Name: api_app_houses_owner_id_251676b2; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_houses_owner_id_251676b2 ON public.api_app_houses USING btree (owner_id);


--
-- Name: api_app_messages_from_user_id_f1e6f2c0; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_messages_from_user_id_f1e6f2c0 ON public.api_app_messages USING btree (from_user_id);


--
-- Name: api_app_messages_to_user_id_78224509; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_messages_to_user_id_78224509 ON public.api_app_messages USING btree (to_user_id);


--
-- Name: api_app_orders_house_id_4a3a35c3; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_orders_house_id_4a3a35c3 ON public.api_app_orders USING btree (house_id);


--
-- Name: api_app_orders_user_id_3bf145e8; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_orders_user_id_3bf145e8 ON public.api_app_orders USING btree (user_id);


--
-- Name: api_app_testimonials_house_id_64adb7de; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_testimonials_house_id_64adb7de ON public.api_app_testimonials USING btree (house_id);


--
-- Name: api_app_testimonials_user_id_56a7ad30; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_testimonials_user_id_56a7ad30 ON public.api_app_testimonials USING btree (user_id);


--
-- Name: api_app_user_city_id_5fb474e2; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_user_city_id_5fb474e2 ON public.api_app_user USING btree (city_id);


--
-- Name: api_app_user_groups_group_id_426b7dc7; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_user_groups_group_id_426b7dc7 ON public.api_app_user_groups USING btree (group_id);


--
-- Name: api_app_user_groups_user_id_390fed33; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_user_groups_user_id_390fed33 ON public.api_app_user_groups USING btree (user_id);


--
-- Name: api_app_user_user_permissions_permission_id_d1f027c8; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_user_user_permissions_permission_id_d1f027c8 ON public.api_app_user_user_permissions USING btree (permission_id);


--
-- Name: api_app_user_user_permissions_user_id_761cb4cb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_user_user_permissions_user_id_761cb4cb ON public.api_app_user_user_permissions USING btree (user_id);


--
-- Name: api_app_user_username_110f8457_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX api_app_user_username_110f8457_like ON public.api_app_user USING btree (username varchar_pattern_ops);


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
-- Name: api_app_cities api_app_cities_country_id_6ac39f3b_fk_api_app_countries_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_cities
	ADD CONSTRAINT api_app_cities_country_id_6ac39f3b_fk_api_app_countries_id FOREIGN KEY (country_id) REFERENCES public.api_app_countries(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_house_facilities api_app_house_facili_facility_id_c3df75b1_fk_api_app_f; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_house_facilities
	ADD CONSTRAINT api_app_house_facili_facility_id_c3df75b1_fk_api_app_f FOREIGN KEY (facility_id) REFERENCES public.api_app_facilities(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_house_facilities api_app_house_facilities_house_id_b43f1271_fk_api_app_houses_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_house_facilities
	ADD CONSTRAINT api_app_house_facilities_house_id_b43f1271_fk_api_app_houses_id FOREIGN KEY (house_id) REFERENCES public.api_app_houses(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_house_photos api_app_house_photos_house_id_ac6edd9e_fk_api_app_houses_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_house_photos
	ADD CONSTRAINT api_app_house_photos_house_id_ac6edd9e_fk_api_app_houses_id FOREIGN KEY (house_id) REFERENCES public.api_app_houses(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_houses api_app_houses_city_id_0a2f69c4_fk_api_app_cities_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_houses
	ADD CONSTRAINT api_app_houses_city_id_0a2f69c4_fk_api_app_cities_id FOREIGN KEY (city_id) REFERENCES public.api_app_cities(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_houses api_app_houses_owner_id_251676b2_fk_api_app_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_houses
	ADD CONSTRAINT api_app_houses_owner_id_251676b2_fk_api_app_user_id FOREIGN KEY (owner_id) REFERENCES public.api_app_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_messages api_app_messages_from_user_id_f1e6f2c0_fk_api_app_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_messages
	ADD CONSTRAINT api_app_messages_from_user_id_f1e6f2c0_fk_api_app_user_id FOREIGN KEY (from_user_id) REFERENCES public.api_app_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_messages api_app_messages_to_user_id_78224509_fk_api_app_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_messages
	ADD CONSTRAINT api_app_messages_to_user_id_78224509_fk_api_app_user_id FOREIGN KEY (to_user_id) REFERENCES public.api_app_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_orders api_app_orders_house_id_4a3a35c3_fk_api_app_houses_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_orders
	ADD CONSTRAINT api_app_orders_house_id_4a3a35c3_fk_api_app_houses_id FOREIGN KEY (house_id) REFERENCES public.api_app_houses(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_orders api_app_orders_user_id_3bf145e8_fk_api_app_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_orders
	ADD CONSTRAINT api_app_orders_user_id_3bf145e8_fk_api_app_user_id FOREIGN KEY (user_id) REFERENCES public.api_app_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_testimonials api_app_testimonials_house_id_64adb7de_fk_api_app_houses_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_testimonials
	ADD CONSTRAINT api_app_testimonials_house_id_64adb7de_fk_api_app_houses_id FOREIGN KEY (house_id) REFERENCES public.api_app_houses(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_testimonials api_app_testimonials_user_id_56a7ad30_fk_api_app_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_testimonials
	ADD CONSTRAINT api_app_testimonials_user_id_56a7ad30_fk_api_app_user_id FOREIGN KEY (user_id) REFERENCES public.api_app_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_user api_app_user_city_id_5fb474e2_fk_api_app_cities_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user
	ADD CONSTRAINT api_app_user_city_id_5fb474e2_fk_api_app_cities_id FOREIGN KEY (city_id) REFERENCES public.api_app_cities(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_user_groups api_app_user_groups_group_id_426b7dc7_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user_groups
	ADD CONSTRAINT api_app_user_groups_group_id_426b7dc7_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_user_groups api_app_user_groups_user_id_390fed33_fk_api_app_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user_groups
	ADD CONSTRAINT api_app_user_groups_user_id_390fed33_fk_api_app_user_id FOREIGN KEY (user_id) REFERENCES public.api_app_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_user_user_permissions api_app_user_user_pe_permission_id_d1f027c8_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user_user_permissions
	ADD CONSTRAINT api_app_user_user_pe_permission_id_d1f027c8_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: api_app_user_user_permissions api_app_user_user_pe_user_id_761cb4cb_fk_api_app_u; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.api_app_user_user_permissions
	ADD CONSTRAINT api_app_user_user_pe_user_id_761cb4cb_fk_api_app_u FOREIGN KEY (user_id) REFERENCES public.api_app_user(id) DEFERRABLE INITIALLY DEFERRED;


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
-- PostgreSQL database dump complete
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

COPY public.api_app_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, sex, type, photo, city_id) FROM stdin;
3	pbkdf2_sha256$260000$CFVIUvf4HPqkBJjyRbB4IL$/RBAKMKeahsBvnAX1SvlRud2vxUkagW+c6URVVLkB1k=	2021-10-02 02:21:21.408406+03	f	owner	Маша	Светлова		f	t	2021-10-02 02:21:13.921859+03	f	owner	db_cw/files/media/lilo-and-stitch_70EPAuK.jpg	1
4	pbkdf2_sha256$260000$KsvIxcWxrtVCZ4Kh6wgsA1$yMuggdxYGCeb5zEZJorJd1kX3jU24oqBOYpoCl9bB6s=	2021-10-02 02:32:15.942906+03	f	owner2	Гена	Петров		f	t	2021-10-02 02:32:10.400382+03	m	owner	db_cw/files/media/avatar1.jpeg	5
2	pbkdf2_sha256$260000$krAX6zhWtvaCmAMdsovjgy$X4NQk5OfqrSW8zvZc6rKWuolGn610Rv7sxOd1RWIqoA=	2021-10-02 03:03:46.526095+03	f	guest	Василий	Макаров		f	t	2021-10-02 02:20:22.962286+03	m	guest	db_cw/files/media/unnamed_0EwUUXT.jpeg	1
6	pbkdf2_sha256$260000$Wha5xfjuyJln9szVkYAW3P$4YfL47alotglivB2GUl5vz7iglD+Jm6EjgxBk4BLAI8=	2021-10-02 03:31:56.390037+03	f	owner10	Геннадий	Макаров		f	t	2021-10-02 03:09:03.631807+03	m	owner	db_cw/files/media/avatar5.jpeg	9
1	pbkdf2_sha256$260000$2W4rOgwqBBcybDOJp21VoB$q+ZPuaFsbcsHpc4uM9XOyEIteiIMRSE9JfDTSflZUwI=	2021-10-02 03:41:42.207673+03	t	admin	Егор	Панафидин	admin@gmail.com	t	t	2021-10-02 02:19:47.763178+03	m	admin	db_cw/files/media/unnamed_0EwUUXT.jpeg	1
5	pbkdf2_sha256$260000$rybSFp8bJ0aGV1S5Wy47rF$hU6/MBLojcvj7uzqiARtegGYM90NhcWUPRopoX7ah64=	2021-10-02 10:47:57.748848+03	f	guest10	Света	Иванова		f	t	2021-10-02 03:06:47.221128+03	f	guest	db_cw/files/media/avatar3.jpeg	5
\.


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


COPY public.api_app_house_photos (id, photo, house_id) FROM stdin;
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
