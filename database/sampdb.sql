-- SEQUENCE: public.president_id_seq

-- DROP SEQUENCE IF EXISTS public.president_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.president_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1
    OWNED BY president.id;

ALTER SEQUENCE public.president_id_seq
    OWNER TO postgres;

-- Table: public.president

-- DROP TABLE IF EXISTS public.president;

CREATE TABLE IF NOT EXISTS public.president
(
    id integer NOT NULL DEFAULT nextval('president_id_seq'::regclass),
    last_name character varying(15) COLLATE pg_catalog."default" NOT NULL,
    first_name character varying(15) COLLATE pg_catalog."default" NOT NULL,
    suffix character varying(5) COLLATE pg_catalog."default",
    city character varying(20) COLLATE pg_catalog."default" NOT NULL,
    state character varying(2) COLLATE pg_catalog."default" NOT NULL,
    birth date NOT NULL,
    death date,
    CONSTRAINT president_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.president
    OWNER to postgres;



-- Table: public.picture

-- DROP TABLE IF EXISTS public.picture;

CREATE TABLE IF NOT EXISTS public.picture
(
    pict_id integer NOT NULL,
    pict_icon character varying(20) COLLATE pg_catalog."default",
    pict_data character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT picture_pkey PRIMARY KEY (pict_id),
    CONSTRAINT picture_president_fk FOREIGN KEY (pict_id)
        REFERENCES public.president (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.picture
    OWNER to postgres;