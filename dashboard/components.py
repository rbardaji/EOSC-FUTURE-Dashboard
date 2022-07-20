from dash import html, dcc

import yaml_service
import text

# Init DTOs
YDTO = yaml_service.YamlDataTransferObject()

# Components
providers_checklist = dcc.Checklist(
    id='providers-checklist',
    className='providers-checklist',
    options=YDTO.get_providers(),
    inputClassName='input-providers-checklist',
    labelClassName='label-providers-checklist'
)

main_layout = html.Div(
    children=[
        dcc.Store(
            id='local-state',
            storage_type='local'
        ),
        html.Div(
            className='header-container',
            children=[
                html.Div(
                    className='flex-child-image',
                    children=[
                        html.Img(
                            className='header-image',
                            src='https://eoscfuture.eu/wp-content/themes/eosc/assets/img/logos/eosc-future.svg'
                        )
                    ]
                ),
                html.Div(
                    className='flex-child-headings',
                    children=[
                        html.H1(text.title),
                        html.H2(text.subtitle)
                    ]
                )
            ]
        ),
        providers_checklist,
        html.Div(
            id='my-output',
            className='output'
        ),
    ]
)
