import os.path

import click  # type: ignore

from plume_python import parser
from plume_python.export.xdf_exporter import export_xdf_from_record
from plume_python.samples import sample_types_from_names
from plume_python.utils.dataframe import (
    record_to_dataframes,
    samples_to_dataframe,
    world_transforms_to_dataframe,
)
from plume_python.utils.game_object import (
    find_names_by_guid,
    find_identifiers_by_name,
    find_identifier_by_game_object_id,
)
from plume_python.utils.transform import compute_transform_time_series


@click.group()
def cli():
    pass


@click.command()
@click.argument("record_path", type=click.Path(exists=True, readable=True))
@click.option("--xdf_output_path", type=click.Path(writable=True))
def export_xdf(record_path: str, xdf_output_path: str | None):
    """Export a XDF file including LSL samples and markers."""
    if not record_path.endswith(".plm"):
        click.echo(err=True, message="Input file must be a .plm file")
        return

    if xdf_output_path is None:
        xdf_output_path = record_path.replace(".plm", ".xdf")

    if os.path.exists(xdf_output_path):
        if not click.confirm(
            f"File '{xdf_output_path}' already exists, do you want to overwrite it?"
        ):
            return

    with open(xdf_output_path, "wb") as xdf_output_file:
        record = parser.parse_record_from_file(record_path)
        export_xdf_from_record(xdf_output_file, record)
        click.echo(
            "Exported xdf from record: "
            + record_path
            + " to "
            + xdf_output_path
        )


@click.command()
@click.argument("record_path", type=click.Path(exists=True, readable=True))
@click.argument("guid", type=click.STRING)
def find_name(record_path: str, guid: str):
    """Find the name(s) of a GameObject with the given GUID in the record."""
    if not record_path.endswith(".plm"):
        click.echo(err=True, message="Input file must be a .plm file")
        return

    record = parser.parse_record_from_file(record_path)
    names = find_names_by_guid(record, guid)
    if names:
        click.echo(f"Found {len(names)} name(s) for GUID {guid}:")
        for name in names:
            click.echo(name)
    else:
        click.echo(f"No name found for GUID {guid}")


@click.command()
@click.argument("record_path", type=click.Path(exists=True, readable=True))
@click.argument("name", type=click.STRING)
def find_guid(record_path: str, name: str):
    """Find the GUID(s) of a GameObject by the given name."""
    if not record_path.endswith(".plm"):
        click.echo(err=True, message="Input file must be a .plm file")
        return

    record = parser.parse_record_from_file(record_path)
    identifiers = find_identifiers_by_name(record, name)
    if identifiers:
        click.echo(f"Found {len(identifiers)} GUID(s) for name {name}:")
        for identifier in identifiers:
            click.echo(identifier.game_object_id)
    else:
        click.echo(f"No GUID found for name {name}")


@click.command()
@click.argument("record_path", type=click.Path(exists=True, readable=True))
@click.argument("guid", type=click.STRING)
def export_world_transforms(record_path: str, guid: str):
    """Export world transforms of a GameObject with the given GUID to a CSV file."""
    if not record_path.endswith(".plm"):
        click.echo(err=True, message="Input file must be a .plm file")
        return

    record = parser.parse_record_from_file(record_path)
    identifier = find_identifier_by_game_object_id(record, guid)

    if identifier is None:
        click.echo(err=True, message=f"No identifier found for GUID {guid}")
        return

    time_series = compute_transform_time_series(
        record, identifier.transform_id
    )
    df = world_transforms_to_dataframe(time_series)
    file_path = record_path.replace(".plm", f"_{guid}_world_transform.csv")
    df.to_csv(file_path)


@click.command()
@click.argument("record_path", type=click.Path(exists=True, readable=True))
@click.argument("output_dir", type=click.Path(exists=True, writable=True))
@click.option(
    "--filter",
    default="all",
    show_default=True,
    type=click.STRING,
    help="Comma separated list of sample types to export (eg. 'TransformUpdate,GameObjectUpdate')",
)
def export_csv(record_path: str, output_dir: str | None, filter: str):
    """Export samples from the record to CSV files."""
    if not record_path.endswith(".plm"):
        click.echo(err=True, message="Input file must be a .plm file")
        return

    record = parser.parse_record_from_file(record_path)

    filters = [d.strip() for d in filter.split(",")]

    if filters == ["all"] or filters == ["*"]:
        dataframes = record_to_dataframes(record)
        for sample_type, df in dataframes.items():
            file_path = os.path.join(output_dir, sample_type.__name__ + ".csv")
            df.to_csv(file_path)
            click.echo(
                "Exported CSV for sample type: "
                + sample_type.__name__
                + " to "
                + file_path
            )
    else:
        sample_types = sample_types_from_names(filters)
        for sample_type in sample_types:
            df = samples_to_dataframe(record.get_samples_by_type(sample_type))
            file_path = os.path.join(output_dir, sample_type.__name__ + ".csv")
            df.to_csv(file_path)
            click.echo(
                "Exported CSV for sample type: "
                + sample_type.__name__
                + " to "
                + file_path
            )


cli.add_command(export_csv)
cli.add_command(export_xdf)
cli.add_command(find_name)
cli.add_command(find_guid)
cli.add_command(export_world_transforms)
