from django.db import migrations


def set_live_demo_urls(apps, schema_editor):
    Project = apps.get_model("main", "Project")
    urls = {
        "Product Line Profitability & Margin Performance Analysis for Nassau Candy Distributor": "https://nscandyapppy-efjhfamkizdrvz7itx6yjy.streamlit.app/",
        "Care Transition Efficiency & Placement Outcome Analytics": "https://caretransitiondashboardpy-qhwhvv7appvhqjvwccdzll4.streamlit.app/",
    }
    for title, url in urls.items():
        Project.objects.filter(title=title).update(live_demo_url=url)


class Migration(migrations.Migration):
    dependencies = [("main", "0003_alter_sociallink_url")]

    operations = [migrations.RunPython(set_live_demo_urls, migrations.RunPython.noop)]