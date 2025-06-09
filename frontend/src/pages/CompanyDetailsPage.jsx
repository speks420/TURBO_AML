import { useParams, Link as RouterLink, useNavigate } from 'react-router-dom';
import {
  Box,
  Heading,
  Text,
  VStack,
  HStack,
  Badge,
  Divider,
  Button,
  Alert,
  AlertIcon,
  Grid,
  GridItem,
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  TableContainer,
  useDisclosure
} from '@chakra-ui/react';
import { TimeIcon } from '@chakra-ui/icons';
import Layout from '../components/layout/Layout';
import LoadingSpinner from '../components/ui/LoadingSpinner';
import SearchHistoryDrawer from '../components/ui/SearchHistoryDrawer';
import FinancialOverview from '../components/ui/FinancialOverview';
import HealthScoreCard from '../components/ui/HealthScoreCard';
import useCompanyDetails from '../hooks/useCompanyDetails';
import { formatDate, formatStatus, formatRegNumber } from '../utils/formatters';

/**
 * CompanyDetailsPage component
 * 
 * @returns {JSX.Element} CompanyDetailsPage component
 */
const CompanyDetailsPage = () => {
  const { regNumber } = useParams();
  const navigate = useNavigate();
  const { isLoading, error, company, refetch } = useCompanyDetails(regNumber);
  const { isOpen, onOpen, onClose } = useDisclosure();

  const handleCompanySelect = (regNumber) => {
    navigate(`/company/${regNumber}`);
  };

  if (isLoading) {
    return (
      <Layout>
        <LoadingSpinner text="Loading company details..." />
      </Layout>
    );
  }

  if (error) {
    return (
      <Layout>
        <Alert status="error" mb={4}>
          <AlertIcon />
          {error}
        </Alert>
        <Button as={RouterLink} to="/" colorScheme="brand" size="sm">
          Back to Search
        </Button>
      </Layout>
    );
  }

  if (!company) {
    return (
      <Layout>
        <Alert status="info" mb={4}>
          <AlertIcon />
          Company not found or still loading.
        </Alert>
        <Button as={RouterLink} to="/" colorScheme="brand" size="sm">
          Back to Search
        </Button>
      </Layout>
    );
  }

  // Extract company information
  const {
    name,
    registration_number,
    status,
    address,
    founded_date,
    capital_data = [],
    beneficiary_data = [],
    members_data = [],
    business_data = [],
    liquidation_data = [],
    officers_data = [],
    stockholders_data = [],
    taxpayer_ratings = [],
    has_liquidation_process = false,
    is_stock_company = false,
    registry_data = {}
  } = company;

  const formattedStatus = formatStatus(status);
  const formattedRegNumber = formatRegNumber(registration_number);
  const formattedFoundedDate = formatDate(founded_date);

  return (
    <Layout>
      <Box mb={6} display="flex" justifyContent="space-between">
        <Button as={RouterLink} to="/" colorScheme="brand" variant="outline" size="sm">
          ← Back to Search
        </Button>
        <Button 
          rightIcon={<TimeIcon />} 
          colorScheme="brand" 
          variant="outline" 
          size="sm"
          onClick={onOpen}
        >
          Recent Searches
        </Button>
      </Box>

      <SearchHistoryDrawer 
        isOpen={isOpen} 
        onClose={onClose} 
        onCompanySelect={handleCompanySelect} 
      />

      <VStack align="stretch" spacing={6} bg="white" p={6} borderRadius="md" boxShadow="md">
        <HStack justifyContent="space-between" alignItems="flex-start" wrap="wrap">
          <VStack align="start" spacing={1}>
            <Heading as="h1" size="xl" color="brand.700">
              {name}
            </Heading>
            <Text color="gray.600">Registration number: {formattedRegNumber}</Text>
          </VStack>
          <VStack spacing={2} align="end">
            <Badge
              colorScheme={formattedStatus === 'Active' ? 'green' : 'red'}
              p={2}
              borderRadius="md"
              fontSize="md"
            >
              {formattedStatus}
            </Badge>
            <Badge
              colorScheme={has_liquidation_process ? 'red' : 'green'}
              p={2}
              borderRadius="md"
              fontSize="md"
            >
              {has_liquidation_process ? 'Liquidation Process Active' : 'No Liquidation Process'}
            </Badge>
            {is_stock_company && (
              <Badge
                colorScheme="blue"
                p={2}
                borderRadius="md"
                fontSize="md"
              >
                Stock Company (AS)
              </Badge>
            )}
          </VStack>
        </HStack>

        {has_liquidation_process && (
          <Alert status="error" borderRadius="md">
            <AlertIcon />
            <VStack align="start" spacing={1} width="100%">
              <Text fontWeight="bold">Warning: This company has an active liquidation process</Text>
              {liquidation_data.length > 0 && (
                <Text>
                  Type: {liquidation_data[0].liquidation_type_text || 'Unknown'}, 
                  Started: {liquidation_data[0].date_from ? formatDate(liquidation_data[0].date_from) : 'Unknown'}
                </Text>
              )}
            </VStack>
          </Alert>
        )}

        <Divider />

        <Grid templateColumns={{ base: "1fr", md: "repeat(2, 1fr)" }} gap={6}>
          <GridItem>
            <VStack align="start" spacing={4}>
              <Box>
                <Text fontWeight="bold" color="gray.700">Address</Text>
                <Text>{address || 'Not available'}</Text>
              </Box>
              <Box>
                <Text fontWeight="bold" color="gray.700">Founded Date</Text>
                <Text>{formattedFoundedDate}</Text>
              </Box>
            </VStack>
          </GridItem>
          <GridItem>
            <VStack align="start" spacing={4}>
              {/* Example of other fields that might be in registry_data */}
              <Box>
                <Text fontWeight="bold" color="gray.700">Legal Form</Text>
                <Text>{registry_data.legal_form || business_data[0]?.legal_form_code_text || 'Not available'}</Text>
              </Box>
              <Box>
                <Text fontWeight="bold" color="gray.700">Industry</Text>
                <Text>{registry_data.industry || 'Not available'}</Text>
              </Box>
            </VStack>
          </GridItem>
        </Grid>

        <Divider />

        {/* Taxpayer Ratings Section */}
        {taxpayer_ratings && taxpayer_ratings.length > 0 && (
          <>
            <Box>
              <Heading as="h3" size="md" mb={4} color="blue.600">Taxpayer Rating</Heading>
              <Grid templateColumns={{ base: "1fr", md: "repeat(2, 1fr)" }} gap={6}>
                {taxpayer_ratings.map((rating, index) => (
                  <GridItem key={index}>
                    <Box 
                      p={4} 
                      borderWidth="1px" 
                      borderRadius="md" 
                      borderColor="blue.200"
                      bg="blue.50"
                    >
                      <VStack align="start" spacing={3}>
                        <HStack justifyContent="space-between" w="100%">
                          <Text fontWeight="bold" color="blue.700">Rating</Text>
                          <Badge 
                            colorScheme={
                              rating.reitings === 'Augsts' ? 'green' :
                              rating.reitings === 'Vidējs' ? 'yellow' :
                              rating.reitings === 'Zems' ? 'red' : 'gray'
                            }
                            fontSize="md"
                            p={2}
                          >
                            {rating.reitings || 'Not Available'}
                          </Badge>
                        </HStack>
                        
                        {rating.skaidrojums && (
                          <Box>
                            <Text fontWeight="bold" color="gray.700" fontSize="sm">Explanation</Text>
                            <Text fontSize="sm" color="gray.600">
                              {rating.skaidrojums}
                            </Text>
                          </Box>
                        )}
                        
                        {rating.informacijas_atjaunosanas_datums && (
                          <Box>
                            <Text fontWeight="bold" color="gray.700" fontSize="sm">Last Updated</Text>
                            <Text fontSize="sm" color="gray.600">
                              {formatDate(rating.informacijas_atjaunosanas_datums)}
                            </Text>
                          </Box>
                        )}
                      </VStack>
                    </Box>
                  </GridItem>
                ))}
              </Grid>
            </Box>
            <Divider />
          </>
        )}

        {/* Company Officers Data - New Section */}
        {officers_data && officers_data.length > 0 && (
          <>
            <Box>
              <Heading as="h3" size="md" mb={4}>Company Officers</Heading>
              <TableContainer>
                <Table variant="simple" size="sm">
                  <Thead>
                    <Tr>
                      <Th>Name</Th>
                      <Th>Position</Th>
                      <Th>Governing Body</Th>
                      <Th>Entity Type</Th>
                      <Th>Representation Rights</Th>
                      <Th>ID Number</Th>
                      <Th>Registered On</Th>
                    </Tr>
                  </Thead>
                  <Tbody>
                    {officers_data.map((officer, index) => (
                      <Tr key={index}>
                        <Td>{officer.name || '—'}</Td>
                        <Td>{officer.position || '—'}</Td>
                        <Td>{officer.governing_body || '—'}</Td>
                        <Td>{officer.entity_type || '—'}</Td>
                        <Td>{officer.rights_of_representation_type || '—'}</Td>
                        <Td>{officer.latvian_identity_number_masked || officer.legal_entity_registration_number || '—'}</Td>
                        <Td>{officer.registered_on ? formatDate(officer.registered_on) : '—'}</Td>
                      </Tr>
                    ))}
                  </Tbody>
                </Table>
              </TableContainer>
            </Box>
            <Divider />
          </>
        )}

        {/* Stockholders Data - New Section (only for AS type companies) */}
        {is_stock_company && stockholders_data && stockholders_data.length > 0 && (
          <>
            <Box>
              <Heading as="h3" size="md" mb={4}>Stockholders</Heading>
              <TableContainer>
                <Table variant="simple" size="sm">
                  <Thead>
                    <Tr>
                      <Th>Name</Th>
                      <Th>Entity Type</Th>
                      <Th>ID Number/Reg Number</Th>
                      <Th>Shares</Th>
                      <Th>Value</Th>
                      <Th>Votes</Th>
                      <Th>Stock Type</Th>
                      <Th>From Date</Th>
                    </Tr>
                  </Thead>
                  <Tbody>
                    {stockholders_data.map((stockholder, index) => (
                      <Tr key={index}>
                        <Td>{stockholder.name || '—'}</Td>
                        <Td>{stockholder.entity_type || '—'}</Td>
                        <Td>
                          {stockholder.entity_type === 'NATURAL_PERSON' 
                            ? stockholder.latvian_identity_number_masked || '—'
                            : stockholder.legal_entity_registration_number || '—'}
                        </Td>
                        <Td>{stockholder.number_of_shares || '—'}</Td>
                        <Td>
                          {stockholder.share_nominal_value && stockholder.share_currency
                            ? `${stockholder.share_nominal_value} ${stockholder.share_currency}`
                            : '—'}
                        </Td>
                        <Td>{stockholder.votes || '—'}</Td>
                        <Td>{stockholder.stock_type || '—'}</Td>
                        <Td>{stockholder.date_from ? formatDate(stockholder.date_from) : '—'}</Td>
                      </Tr>
                    ))}
                  </Tbody>
                </Table>
              </TableContainer>
            </Box>
            <Divider />
          </>
        )}

        {/* Business Activity Data */}
        {business_data && business_data.length > 0 && (
          <>
            <Box>
              <Heading as="h3" size="md" mb={4}>Business Activities</Heading>
              <TableContainer>
                <Table variant="simple" size="sm">
                  <Thead>
                    <Tr>
                      <Th>Area of Activity</Th>
                      <Th>Legal Form</Th>
                    </Tr>
                  </Thead>
                  <Tbody>
                    {business_data.map((activity, index) => (
                      <Tr key={index}>
                        <Td style={{ whiteSpace: 'normal', wordBreak: 'break-word' }}>
                          {activity.area_of_activity || '—'}
                        </Td>
                        <Td>{activity.legal_form_code_text || activity.legal_form_code || '—'}</Td>
                      </Tr>
                    ))}
                  </Tbody>
                </Table>
              </TableContainer>
            </Box>
            <Divider />
          </>
        )}

        {/* Liquidation Process Data */}
        {liquidation_data && liquidation_data.length > 0 && (
          <>
            <Box>
              <Heading as="h3" size="md" mb={4} color="red.500">Liquidation Processes</Heading>
              <TableContainer>
                <Table variant="simple" size="sm">
                  <Thead>
                    <Tr>
                      <Th>Type</Th>
                      <Th>Started On</Th>
                      <Th>Grounds</Th>
                      <Th>Registered On</Th>
                    </Tr>
                  </Thead>
                  <Tbody>
                    {liquidation_data.map((process, index) => (
                      <Tr key={index}>
                        <Td>{process.liquidation_type_text || process.liquidation_type || '—'}</Td>
                        <Td>{process.date_from ? formatDate(process.date_from) : '—'}</Td>
                        <Td style={{ whiteSpace: 'normal', wordBreak: 'break-word' }}>
                          {process.grounds_for_liquidation || '—'}
                        </Td>
                        <Td>{process.registered_on ? formatDate(process.registered_on) : '—'}</Td>
                      </Tr>
                    ))}
                  </Tbody>
                </Table>
              </TableContainer>
            </Box>
            <Divider />
          </>
        )}

        {/* Beneficial Owners Data */}
        {beneficiary_data && beneficiary_data.length > 0 && (
          <>
            <Box>
              <Heading as="h3" size="md" mb={4}>Beneficial Owners</Heading>
              <TableContainer>
                <Table variant="simple" size="sm">
                  <Thead>
                    <Tr>
                      <Th>Name</Th>
                      <Th>Birth Date</Th>
                      <Th>Nationality</Th>
                      <Th>Residence</Th>
                      <Th>ID Number</Th>
                      <Th>Registered On</Th>
                    </Tr>
                  </Thead>
                  <Tbody>
                    {beneficiary_data.map((owner, index) => (
                      <Tr key={index}>
                        <Td>{owner.forename && owner.surname ? `${owner.forename} ${owner.surname}` : '—'}</Td>
                        <Td>{owner.birth_date || '—'}</Td>
                        <Td>{owner.nationality || '—'}</Td>
                        <Td>{owner.residence || '—'}</Td>
                        <Td>{owner.latvian_identity_number_masked || '—'}</Td>
                        <Td>{owner.registered_on ? formatDate(owner.registered_on) : '—'}</Td>
                      </Tr>
                    ))}
                  </Tbody>
                </Table>
              </TableContainer>
            </Box>
            <Divider />
          </>
        )}

        {/* Company Members Data */}
        {members_data && members_data.length > 0 && (
          <>
            <Box>
              <Heading as="h3" size="md" mb={4}>Company Members</Heading>
              <TableContainer>
                <Table variant="simple" size="sm">
                  <Thead>
                    <Tr>
                      <Th>Name</Th>
                      <Th>Entity Type</Th>
                      <Th>ID Number/Reg Number</Th>
                      <Th>Birth Date</Th>
                      <Th>Shares</Th>
                      <Th>Value</Th>
                      <Th>From Date</Th>
                    </Tr>
                  </Thead>
                  <Tbody>
                    {members_data.map((member, index) => (
                      <Tr key={index}>
                        <Td>{member.name || '—'}</Td>
                        <Td>{member.entity_type || '—'}</Td>
                        <Td>
                          {member.entity_type === 'NATURAL_PERSON' 
                            ? member.latvian_identity_number_masked || '—'
                            : member.legal_entity_registration_number || '—'}
                        </Td>
                        <Td>{member.birth_date || '—'}</Td>
                        <Td>{member.number_of_shares || '—'}</Td>
                        <Td>
                          {member.share_nominal_value && member.share_currency
                            ? `${member.share_nominal_value} ${member.share_currency}`
                            : '—'}
                        </Td>
                        <Td>{member.date_from ? formatDate(member.date_from) : '—'}</Td>
                      </Tr>
                    ))}
                  </Tbody>
                </Table>
              </TableContainer>
            </Box>
            <Divider />
          </>
        )}

        {/* Capital and Investment Data */}
        {capital_data && capital_data.length > 0 && (
          <>
            <Box>
              <Heading as="h3" size="md" mb={4}>Capital and Investment Data</Heading>
              <TableContainer>
                <Table variant="simple" size="sm">
                  <Thead>
                    <Tr>
                      <Th>Capital Type</Th>
                      <Th>Amount</Th>
                      <Th>Currency</Th>
                      <Th>Date</Th>
                    </Tr>
                  </Thead>
                  <Tbody>
                    {capital_data.map((item, index) => (
                      <Tr key={index}>
                        <Td>{item.equity_capital_type_text || item.equity_capital_type || '—'}</Td>
                        <Td>{item.amount || '—'}</Td>
                        <Td>{item.currency || '—'}</Td>
                        <Td>{item.date_from ? formatDate(item.date_from) : '—'}</Td>
                      </Tr>
                    ))}
                  </Tbody>
                </Table>
              </TableContainer>
            </Box>
            <Divider />
          </>
        )}

        {/* Health Score */}
        <HealthScoreCard regNumber={registration_number} />

        {/* Financial Overview */}
        <FinancialOverview regNumber={registration_number} />

        <Box>
          <Heading as="h3" size="md" mb={4}>Full Company Data</Heading>
          <Grid templateColumns={{ base: "1fr", md: "repeat(2, 1fr)" }} gap={4}>
            <GridItem><Text fontWeight="bold">Registration code</Text><Text>{company.regcode || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">SEPA code</Text><Text>{company.sepa || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">Name</Text><Text>{company.name || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">Name (before quotes)</Text><Text>{company.name_before_quotes || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">Name (in quotes)</Text><Text>{company.name_in_quotes || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">Name (after quotes)</Text><Text>{company.name_after_quotes || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">Without quotes</Text><Text>{company.without_quotes || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">Reg type</Text><Text>{company.regtype || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">Reg type text</Text><Text>{company.regtype_text || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">Type</Text><Text>{company.type || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">Type text</Text><Text>{company.type_text || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">Registered</Text><Text>{company.registered || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">Terminated</Text><Text>{company.terminated || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">Closed</Text><Text>{company.closed || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">Address</Text><Text>{company.address || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">Postal index</Text><Text>{company.index || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">Address ID</Text><Text>{company.addressid || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">Region</Text><Text>{company.region || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">City</Text><Text>{company.city || '—'}</Text></GridItem>
            <GridItem><Text fontWeight="bold">ATVK</Text><Text>{company.atvk || '—'}</Text></GridItem>
          </Grid>
        </Box>

        <Divider />

        <Box>
          <Heading as="h3" size="md" mb={4}>
            Additional Information
          </Heading>
          <Text>
            The data shown here is retrieved from the Latvian Business Registry via the data.gov.lv
            CKAN API and supplemented with information from our database.
          </Text>
        </Box>
      </VStack>
    </Layout>
  );
};

export default CompanyDetailsPage; 