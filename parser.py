import csv

def writeXER(r, filename):
    header = ['ERMHDR', '8.0', '2021-11-02', 'Project',	'admin', 'Primavera', 'Admin', 'dbxDatabaseNoName', 'Project Management', 'U.K.']
    with open(filename, 'w', newline='', encoding='utf-8') as output:
        tsv_writer = csv.writer(output, delimiter='\t')
        tsv_writer.writerow(header)
        tsv_writer.writerows(r.currencies.get_tsv())
        tsv_writer.writerows(r.fintmpls.get_tsv())
        tsv_writer.writerows(r.nonworks.get_tsv())
        tsv_writer.writerows(r.obss.get_tsv())
        tsv_writer.writerows(r.pcattypes.get_tsv())
        tsv_writer.writerows(r.resourcecurves.get_tsv())
        tsv_writer.writerows(r.udftypes.get_tsv())
        tsv_writer.writerows(r.accounts.get_tsv())
        tsv_writer.writerows(r.pcatvals.get_tsv())
        tsv_writer.writerows(r.projects.get_tsv())
        tsv_writer.writerows(r.calendars.get_tsv())
        tsv_writer.writerows(r.projpcats.get_tsv())
        tsv_writer.writerows(r.scheduleoptions.get_tsv())
        tsv_writer.writerows(r.wbss.get_tsv())
        tsv_writer.writerows(r.resources.get_tsv())
        tsv_writer.writerows(r.acttypes.get_tsv())
        tsv_writer.writerows(r.resourcerates.get_tsv())
        tsv_writer.writerows(r.activities.get_tsv())
        tsv_writer.writerows(r.actvcodes.get_tsv())
        # PROJCOST
        tsv_writer.writerows(r.relations.get_tsv())
        tsv_writer.writerows(r.taskprocs.get_tsv())
        tsv_writer.writerows(r.activityresources.get_tsv())
        tsv_writer.writerows(r.activitycodes.get_tsv())
        tsv_writer.writerows(r.udfvalues.get_tsv())
        tsv_writer.writerow(['%E'])
