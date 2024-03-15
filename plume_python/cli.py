import os.path

import click

from plume_python import parser
from plume_python.export.xdf_exporter import export_xdf_from_record
from plume_python.samples import sample_types_from_names
from plume_python.utils.dataframe import record_to_dataframes, samples_to_dataframe


@click.group()
def cli():
    pass


@click.command()
@click.argument('record_path', type=click.Path(exists=True, readable=True))
@click.option('--xdf_output_path', type=click.Path(writable=True))
def export_xdf(record_path: str, xdf_output_path: str | None):
    if not record_path.endswith('.plm'):
        click.echo(err=True, message="Input file must be a .plm file")
        return

    if xdf_output_path is None:
        xdf_output_path = record_path.replace('.plm', '.xdf')

    if os.path.exists(xdf_output_path):
        if not click.confirm(f"File '{xdf_output_path}' already exists, do you want to overwrite it?"):
            return

    with open(xdf_output_path, "wb") as xdf_output_file:
        record = parser.parse_record_from_file(record_path)
        export_xdf_from_record(xdf_output_file, record)
        click.echo('Exported xdf from record: ' + record_path + ' to ' + xdf_output_path)


@click.command()
@click.argument('record_path', type=click.Path(exists=True, readable=True))
@click.argument('output_dir', type=click.Path(exists=True, writable=True))
@click.option('--filter', default="all", show_default=True, type=click.STRING,
              help="Comma separated list of sample types to export")
def export_csv(record_path: str, output_dir: str | None, filter: str):
    if not record_path.endswith('.plm'):
        click.echo(err=True, message="Input file must be a .plm file")
        return

    record = parser.parse_record_from_file(record_path)

    filters = [d.strip() for d in filter.split(',')]

    if filters == ['all'] or filters == ['*']:
        dataframes = record_to_dataframes(record)
        for sample_type, df in dataframes.items():
            file_path = os.path.join(output_dir, sample_type.__name__ + '.csv')
            df.to_csv(file_path)
            click.echo('Exported CSV for sample type: ' + sample_type.__name__ + ' to ' + file_path)
    else:
        sample_types = sample_types_from_names(filters)
        for sample_type in sample_types:
            df = samples_to_dataframe(record.get_samples_by_type(sample_type))
            file_path = os.path.join(output_dir, sample_type.__name__ + '.csv')
            print(file_path)
            df.to_csv(file_path)
            click.echo('Exported CSV for sample type: ' + sample_type.__name__ + ' to ' + file_path)


cli.add_command(export_csv)
cli.add_command(export_xdf)

if __name__ == '__main__':
    cli()
