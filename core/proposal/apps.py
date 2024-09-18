from django.apps import AppConfig


class ProposalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.proposal'

    def ready(self):
        import core.proposal.signals.AcceptPurpose.invite_email_when_accept_proposal
        import core.proposal.signals.AcceptPurpose.update_status_project
        import core.proposal.signals.Proposal.newProposal