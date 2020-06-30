# Generated by Django 2.2.9 on 2020-06-28 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200627_1211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='Accommodation',
            new_name='accommodation',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Agent_Company',
            new_name='agent_company',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Agent_Contact',
            new_name='agent_contact',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Any_other_navigational_hazards_in_the_area',
            new_name='any_other_navigational_hazards_in_the_area',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Any_other_service_provider_in_the_same_vicinity',
            new_name='any_other_service_provider_in_the_same_vicinity',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Any_physical_limitations_on_vessel_size',
            new_name='any_physical_limitations_on_vessel_size',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Approval_needed_prior_to_each_STS_operation',
            new_name='approval_authority',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Approval_to_conduct_STS_issued_by',
            new_name='cargoes_permitted',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Fees_to_be_incurred_for_STS_Operations',
            new_name='fees_to_be_incurred_for_STS_operations',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Cargos_permitted',
            new_name='operation_type',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Police',
            new_name='police',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Predominant_current',
            new_name='port_fees_vessels',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Prevailing_winds',
            new_name='predominant_current',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Primary_Fenders',
            new_name='prevailing_winds',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Regulations_to_be_complied_during_the_operation',
            new_name='primary_fenders',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Rubber_Hoses',
            new_name='prior_approval_to_each_STS_operation',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Secondary_Fenders',
            new_name='regulations_to_be_complied_during_the_operation',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Security_Arrangements',
            new_name='rubber_hoses',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Size_of_transfer_area',
            new_name='secondary_fenders',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Storage_Space',
            new_name='security_arrangements',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Support_Craft_Owner',
            new_name='size_of_transfer_area',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Telephone',
            new_name='storage_space',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Transit_time_from_shore_to_STS_location',
            new_name='support_craft_owner',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Tug_Provider_Company',
            new_name='telephone',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Tug_Provider_Contact',
            new_name='transit_time_from_shore_to_STS_location',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Tug_Provider_Vessel_Name',
            new_name='tug_provider_company',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Type_of_operation',
            new_name='tug_provider_contact',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Vessel_Name',
            new_name='tug_provider_vessel_Name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Vessel_sizes_permitted',
            new_name='vessel_name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='What_is_considered_international_waters',
            new_name='vessel_sizes_permitted',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='What_is_considered_port_limits',
            new_name='vessels_size_permitted',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='What_is_the_tidal_range_if_applicable',
            new_name='what_is_considered_international_waters',
        ),
        migrations.AddField(
            model_name='location',
            name='what_is_considered_port_limits',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='what_is_the_tidal_range_if_applicable',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
