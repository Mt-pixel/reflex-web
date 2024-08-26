import reflex as rx
from pcweb.components.icons.icons import get_icon
from pcweb.pages.gallery import gallery
from pcweb.pages.docs import getting_started, hosting
from pcweb.pages.docs.library import library
from pcweb.pages.changelog import changelog
from pcweb.pages.blog import blogs
from pcweb.pages.changelog import changelog
from pcweb.pages.faq import faq
from pcweb.pages.errors import errors
from pcweb.components.logo import logo
from pcweb.signup import IndexState
from pcweb.constants import (
    ROADMAP_URL,
    GITHUB_DISCUSSIONS_URL,
    GITHUB_URL,
    TWITTER_URL,
    DISCORD_URL,
)


def footer_link(text: str, href: str) -> rx.Component:
    return rx.link(
        text,
        href=href,
        class_name="font-small text-slate-9 hover:!text-slate-11 no-underline transition-color",
    )


def footer_link_flex(heading: str, links: list[rx.Component]) -> rx.Component:
    return rx.box(
        rx.el.h4(
            heading,
            class_name="text-slate-12 font-smbold",
        ),
        *links,
        class_name="flex flex-col gap-4",
    )


def social_menu_item(icon: str, url: str = "/", border: bool = False) -> rx.Component:
    return rx.link(
        rx.box(
            get_icon(icon=icon),
            class_name="flex justify-center items-center text-slate-9 gap-2 bg-slate-1 hover:bg-slate-3 p-[0.125rem_0.75rem] transition-bg cursor-pointer overflow-hidden"
            + (" border-x border-slate-5" if border else ""),
        ),
        class_name="flex w-full",
        href=url,
        is_external=True,
    )


def menu_socials() -> rx.Component:
    return rx.el.div(
        rx.box(
            social_menu_item("github", GITHUB_URL),
            social_menu_item("twitter", TWITTER_URL, border=True),
            social_menu_item("discord", DISCORD_URL),
            class_name="flex flex-row gap-0 h-full align-center",
        ),
        class_name="md:border-slate-5 bg-slate-3 md:bg-slate-1 shadow-none md:shadow-large md:border rounded-lg md:rounded-[20px] h-6 overflow-hidden",
    )


def newsletter_form() -> rx.Component:
    return (
        rx.box(
            rx.el.h4(
                "Join Newsletter",
                class_name="font-instrument-sans font-semibold text-slate-12 text-sm leading-tight",
            ),
            rx.text(
                "Get the latest updates and news about Reflex.",
                class_name="font-small text-slate-9",
            ),
            rx.cond(
                IndexState.signed_up,
                rx.box(
                    rx.box(
                        rx.icon(
                            tag="circle-check",
                            size=16,
                            class_name="!text-violet-9",
                        ),
                        rx.text(
                            "Thanks for subscribing!",
                            class_name="font-smbold text-slate-11",
                        ),
                        class_name="flex flex-row gap-2 items-center",
                    ),
                    rx.el.button(
                        "Sign up for another email",
                        class_name="bg-slate-3 hover:bg-slate-4 px-3 py-2 rounded-[10px] font-small text-slate-9 cursor-pointer",
                        on_click=IndexState.signup_for_another_user,
                    ),
                    class_name="flex flex-col flex-wrap gap-2",
                ),
                rx.form(
                    rx.box(
                        rx.el.input(
                            placeholder="Your email",
                            name="input_email",
                            type="email",
                            class_name="box-border border-slate-5 focus:border-violet-9 focus:border-1 bg-white-1 p-[0.5rem_0.75rem] border rounded-[10px] font-small text-slate-11 placeholder:text-slate-9 outline-none focus:outline-none",
                        ),
                        rx.form.submit(
                            rx.el.button(
                                "Subscribe",
                                class_name="flex justify-center items-center bg-slate-4 hover:bg-slate-5 p-[0.5rem_0.875rem] rounded-[10px] font-smbold text-slate-9 transition-bg cursor-pointer",
                            ),
                            as_child=True,
                        ),
                        class_name="flex flex-row gap-2 align-center",
                    ),
                    on_submit=IndexState.signup,
                ),
            ),
            class_name="flex flex-col gap-4 align-start",
        ),
    )


@rx.memo
def footer() -> rx.Component:
    return rx.el.footer(
        rx.box(
            rx.box(
                menu_socials(),
                rx.text(
                    "© 2024 Pynecone, Inc.",
                    class_name="font-small text-slate-9",
                ),
                class_name="flex flex-col justify-between gap-4 items-start self-stretch",
            ),
            footer_link_flex(
                "Links",
                [
                    footer_link("Home", "/"),
                    footer_link("Showcase", gallery.path),
                    footer_link("Blog", blogs.path),
                    footer_link("Changelog", changelog.path),
                ],
            ),
            footer_link_flex(
                "Documentation",
                [
                    footer_link("Introduction", getting_started.introduction.path),
                    footer_link("Installation", getting_started.installation.path),
                    footer_link("Components", library.path),
                    footer_link("Hosting", hosting.deploy_quick_start.path),
                ],
            ),
            footer_link_flex(
                "Resources",
                [
                    footer_link("FAQ", faq.path),
                    footer_link("Common Errors", errors.path),
                    footer_link("Roadmap", ROADMAP_URL),
                    footer_link("Forum", GITHUB_DISCUSSIONS_URL),
                ],
            ),
            newsletter_form(),
            class_name="flex flex-row flex-wrap justify-between gap-[4.5rem] w-full max-w-[94.5rem] p-[3rem_1rem_3rem_1.5rem]",
        ),
        class_name="flex border-slate-4 border-t w-full justify-center",
    )
